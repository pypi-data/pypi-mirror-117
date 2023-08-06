"use strict";
(self["webpackChunkjupyterlab_filebrowser_terminal"] = self["webpackChunkjupyterlab_filebrowser_terminal"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__);

/**
 * Initialization data for the jupyterlab-filebrowser-terminal extension.
 */
const plugin = {
    id: 'jupyterlab-filebrowser-terminal:plugin',
    autoStart: true,
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__.ISettingRegistry],
    activate: (app, settingRegistry) => {
        console.log('JupyterLab extension jupyterlab-filebrowser-terminal is activated!');
        app.commands
            .execute('terminal:create-new')
            .then((terminal) => {
            let data = "cd /root";
            terminal.session.send({
                type: 'stdin',
                content: [data]
            });
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.3dead9344fc08a5d76a5.js.map