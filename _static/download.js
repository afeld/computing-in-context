// workaround for
// https://github.com/executablebooks/sphinx-book-theme/issues/863
window.addEventListener("load", () => {
  const links = document.querySelectorAll(
    '.dropdown-download-buttons a[href$=".ipynb"]'
  );

  for (const link of links) {
    link.setAttribute("download", "");
  }
});
