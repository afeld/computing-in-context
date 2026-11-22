const fs = require("fs/promises");
const path = require("path");
const MarkdownIt = require("markdown-it");
const hljs = require("highlight.js");

const markdown = new MarkdownIt({
  html: true,
  linkify: true,
  breaks: true,
  highlight(code, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        const highlighted = hljs.highlight(code, { language: lang }).value;
        return `<pre class="hljs"><code class="language-${lang}">${highlighted}</code></pre>`;
      } catch (err) {
        // fall through to escaped output below
      }
    }
    const escaped = markdown.utils.escapeHtml(code);
    return `<pre class="hljs"><code>${escaped}</code></pre>`;
  }
});

function escapeHtml(value) {
  return markdown.utils.escapeHtml(String(value ?? ""));
}

function normalizeLines(value) {
  if (Array.isArray(value)) return value.join("");
  if (value === undefined || value === null) return "";
  return String(value);
}

function renderStreamOutput(output) {
  const text = normalizeLines(output.text || "");
  if (!text) return "";
  return `<pre class="cell-output stream">${escapeHtml(text)}</pre>`;
}

function renderErrorOutput(output) {
  const traceback = normalizeLines(output.traceback?.join("\n") || output.evalue || output.ename || "");
  if (!traceback) return "";
  return `<pre class="cell-output error">${escapeHtml(traceback)}</pre>`;
}

function renderDisplayData(data) {
  if (!data || typeof data !== "object") return "";

  if (data["text/html"]) {
    return normalizeLines(data["text/html"]);
  }

  const png = data["image/png"];
  if (png) {
    return `<img class="cell-output image" src="data:image/png;base64,${png}" alt="Notebook output"/>`;
  }

  const jpeg = data["image/jpeg"];
  if (jpeg) {
    return `<img class="cell-output image" src="data:image/jpeg;base64,${jpeg}" alt="Notebook output"/>`;
  }

  if (data["text/plain"]) {
    const text = normalizeLines(data["text/plain"]);
    return `<pre class="cell-output text">${escapeHtml(text)}</pre>`;
  }

  const firstMime = Object.keys(data)[0];
  if (!firstMime) return "";

  const fallback = data[firstMime];
  const serialized = typeof fallback === "string" ? fallback : JSON.stringify(fallback, null, 2);
  return `<pre class="cell-output text">${escapeHtml(serialized)}</pre>`;
}

function renderOutput(output) {
  if (!output) return "";

  if (output.output_type === "stream") {
    return renderStreamOutput(output);
  }

  if (output.output_type === "error") {
    return renderErrorOutput(output);
  }

  if (output.output_type === "display_data" || output.output_type === "execute_result") {
    return renderDisplayData(output.data);
  }

  return "";
}

function renderOutputs(outputs) {
  if (!outputs || outputs.length === 0) return "";

  const rendered = outputs
    .map(renderOutput)
    .filter(Boolean)
    .join("\n");

  if (!rendered) return "";

  return `<div class="cell-outputs">${rendered}</div>`;
}

function resolveLanguage(cell) {
  return (
    cell?.metadata?.language ||
    cell?.metadata?.kernelspec?.language ||
    cell?.language ||
    "python"
  );
}

function renderMarkdownCell(cell) {
  const body = markdown.render(normalizeLines(cell.source));
  return `<section class="cell markdown-cell">${body}</section>`;
}

function renderCodeCell(cell) {
  const language = resolveLanguage(cell);
  const source = normalizeLines(cell.source || "");
  const code = markdown.options.highlight(source, language);
  const outputs = renderOutputs(cell.outputs);
  return `<section class="cell code-cell">${code}${outputs}</section>`;
}

function renderCell(cell) {
  if (!cell) return "";
  if (cell.cell_type === "markdown") return renderMarkdownCell(cell);
  if (cell.cell_type === "code") return renderCodeCell(cell);
  return "";
}

function renderNotebook(notebook) {
  const cells = notebook?.cells || [];
  const renderedCells = cells.map(renderCell).filter(Boolean).join("\n\n");
  return `<article class="notebook">${renderedCells}</article>`;
}

async function loadNotebook(inputPath) {
  const raw = await fs.readFile(inputPath, "utf8");
  return JSON.parse(raw);
}

function ipynbPlugin(eleventyConfig) {
  eleventyConfig.addTemplateFormats("ipynb");
  eleventyConfig.addExtension("ipynb", {
    key: "ipynb",
    outputFileExtension: "html",
    read: false,
    async getData(inputPath) {
      const notebook = await loadNotebook(inputPath);
      const slug = path.basename(inputPath, ".ipynb");
      return {
        title: notebook?.metadata?.title || slug
      };
    },
    async compile(_inputContent, inputPath) {
      const notebook = await loadNotebook(inputPath);
      const rendered = renderNotebook(notebook);
      return () => rendered;
    }
  });
}

module.exports = {
  ipynbPlugin,
  renderNotebook
};
