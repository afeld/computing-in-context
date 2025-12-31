const markdownIt = require("markdown-it");
const hljs = require("highlight.js");
const { ipynbPlugin } = require("./src/eleventy-ipynb");

module.exports = function (eleventyConfig) {
  const md = markdownIt({
    html: true,
    linkify: true,
    breaks: true,
    highlight(str, lang) {
      if (lang && hljs.getLanguage(lang)) {
        try {
          const highlighted = hljs.highlight(str, { language: lang }).value;
          return `<pre class="hljs"><code class="language-${lang}">${highlighted}</code></pre>`;
        } catch (err) {
          // fall through to escaped output below
        }
      }
      const escaped = md.utils.escapeHtml(str);
      return `<pre class="hljs"><code>${escaped}</code></pre>`;
    },
  });

  eleventyConfig.setLibrary("md", md);

  eleventyConfig.addPlugin(ipynbPlugin);

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
