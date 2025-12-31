const path = require("node:path");
const { execFile } = require("node:child_process");
const { promisify } = require("node:util");

const execFileAsync = promisify(execFile);

const pythonInterpreter = (() => {
  if (process.env.PYTHON) return process.env.PYTHON;
  if (process.env.VIRTUAL_ENV) {
    return path.join(process.env.VIRTUAL_ENV, "bin", "python");
  }
  return "python";
})();

async function renderNotebookWithNbconvert(inputPath) {
  const { stdout } = await execFileAsync(
    pythonInterpreter,
    [
      "-m",
      "nbconvert",
      "--to",
      "html",
      "--template",
      "lab",
      "--stdout",
      inputPath,
    ],
    { maxBuffer: 100 * 1024 * 1024 }
  );
  return stdout;
}

module.exports = function (eleventyConfig) {
  eleventyConfig.addExtension("ipynb", {
    key: "ipynb",
    outputFileExtension: "html",
    read: false,
    async getData() {
      return {
        layout: null,
      };
    },
    async compile(_content, inputPath) {
      const html = await renderNotebookWithNbconvert(inputPath);
      return () => html;
    },
  });

  eleventyConfig.addGlobalData("layout", "layouts/base.njk");

  eleventyConfig.addPassthroughCopy({
    assets: "assets",
    img: "img",
    data: "data",
  });

  eleventyConfig.addWatchTarget("assets");
  eleventyConfig.addWatchTarget("img");
  eleventyConfig.addWatchTarget("data");

  return {
    dir: {
      input: "pages",
      output: "_site",
      includes: "../_includes",
      data: "../_data",
    },
    templateFormats: ["md", "html", "njk", "ipynb"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
