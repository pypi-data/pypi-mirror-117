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

function changeTerminalDir(session, path) {
    // Send
    session.send({
        type: 'stdin',
        content: [`cd ${path}\n`]
    });
}
/**
 * Initialization data for the jupyterlab-filebrowser-terminal extension.
 */
const plugin = {
    id: 'jupyterlab-filebrowser-terminal:plugin',
    autoStart: true,
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__.IFileBrowserFactory],
    activate: (app, fileBrowserFactory) => {
        // Get filebrowser tracker
        const { tracker } = fileBrowserFactory;
        // Get current filebrowser path
        function getCurrentPath() {
            const widget = tracker.currentWidget;
            return widget.model.path;
        }
        // Add command to open in terminal
        const command = 'filebrowser:open-in-terminal';
        app.commands.addCommand(command, {
            label: 'Open in Terminal',
            execute: () => {
                app.commands
                    .execute('terminal:create-new')
                    .then((widget) => {
                    const terminal = widget.content;
                    const path = getCurrentPath();
                    changeTerminalDir(terminal.session, path);
                });
            },
            isEnabled: () => app.serviceManager.terminals.isAvailable()
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
//# sourceMappingURL=lib_index_js.801fda6a67116ba277ad.js.map