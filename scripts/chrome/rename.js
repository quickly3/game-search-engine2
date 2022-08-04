const webp = require("webp-converter");

const { readdirSync, renameSync, unlinkSync } = require("fs");

const getDirectories = (source) =>
  readdirSync(source, { withFileTypes: true })
    .filter((dirent) => dirent.isDirectory())
    .map((dirent) => dirent.name);

const getFiles = (source) =>
  readdirSync(source, { withFileTypes: true })
    .filter((dirent) => dirent.isFile())
    .map((file) => file.name);

const path = "H:\\迅雷下载\\capoo\\08";

// const dirs = getDirectories(path);

// for (const dir of dirs) {
//   const _dir = path + "\\" + dir;
//   const files = getFiles(_dir);
//   for (const file of files) {
//     const _file = _dir + "\\" + file;
//     console.log(_file);
//   }
// }

const files = getFiles(path);

for (const file of files) {
  const _file = path + "\\" + file;

  if (_file.indexOf(".jpg" > 0)) {
    const newFile = _file.replace(".jpg", ".gif");
    renameSync(_file, newFile);
    continue;
  }

  if (_file.indexOf(".webp" > 0)) {
    const newFile2 = _file.replace(".webp", ".jpg");
    const result = webp.dwebp(_file, newFile2, "-o", (logging = "-v"));
    result.then((response) => {
      unlinkSync(_file);
    });
  }
}
