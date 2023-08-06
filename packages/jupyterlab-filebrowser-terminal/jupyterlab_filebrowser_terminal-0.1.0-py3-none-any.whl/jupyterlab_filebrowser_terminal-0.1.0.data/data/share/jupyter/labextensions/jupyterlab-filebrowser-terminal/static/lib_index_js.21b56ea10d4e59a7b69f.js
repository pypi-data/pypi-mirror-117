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
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Initialization data for the jupyterlab-filebrowser-terminal extension.
 */
const plugin = {
    id: 'jupyterlab-filebrowser-terminal:plugin',
    autoStart: true,
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__.IFileBrowserFactory],
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__.ISettingRegistry],
    activate: (app, fileBrowserFactory, settingRegistry) => {
        console.log('JupyterLab extension jupyterlab-filebrowser-terminal is activated!');
        // Get filebrowser tracker
        const { tracker } = fileBrowserFactory;
        function getCurrentPath() {
            const widget = tracker.currentWidget;
            return widget.model.path;
        }
        // Add an application command
        const command = 'filebrowser:open-terminal';
        app.commands.addCommand(command, {
            label: 'Open in Terminal',
            execute: () => {
                app.commands
                    .execute('terminal:create-new')
                    .then((widget) => {
                    const terminal = widget.content;
                    let session = terminal.session;
                    const path = getCurrentPath();
                    session.connectionStatusChanged.connect((_, change) => {
                        if (change !== "connected") {
                            console.log(change);
                            return;
                        }
                        session.send({
                            type: 'stdin',
                            content: [`cd ${path}\r`]
                        });
                    });
                });
            }
        });
        app.contextMenu.addItem({
            command: command,
            selector: '.jp-DirListing-content'
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.21b56ea10d4e59a7b69f.js.map