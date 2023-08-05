"use strict";
(self["webpackChunk_pachyderm_jupyterlab_pachyderm_theme"] = self["webpackChunk_pachyderm_jupyterlab_pachyderm_theme"] || []).push([["lib_index_js-webpack_sharing_consume_default_lumino_coreutils-webpack_sharing_consume_default-afeeb2"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/polling */ "./node_modules/@lumino/polling/dist/index.es6.js");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_5__);






// const FACTORY = 'Editor';
const ICON_CLASS = 'jp-MainLogo';
const PALETTE_CATEGORY = 'Text Editor';
/**
 * The interval in milliseconds before recover options appear during splash.
 */
const SPLASH_RECOVER_TIMEOUT = 12000;
/**
 * The command IDs used by the apputils plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.loadState = 'apputils:load-statedb';
    CommandIDs.print = 'apputils:print';
    CommandIDs.reset = 'apputils:reset';
    CommandIDs.resetOnLoad = 'apputils:reset-on-load';
    CommandIDs.runFirstEnabled = 'apputils:run-first-enabled';
    CommandIDs.createNew = 'fileeditor:create-new-python-file';
})(CommandIDs || (CommandIDs = {}));
let head = document.head || document.getElementsByTagName('head')[0];
function changeFavicon(src) {
    let link = document.createElement('link'), oldLink = document.getElementById('dynamic-favicon');
    link.id = 'dynamic-favicon';
    link.rel = 'icon';
    link.type = 'image/x-icon';
    link.href = src;
    if (oldLink) {
        head.removeChild(oldLink);
    }
    head.appendChild(link);
    if (document.title != "Notebooks Beta - Pachyderm Hub") {
        document.title = "Notebooks Beta - Pachyderm Hub";
    }
}
const plugin = {
    id: 'jupyterlab-pachyderm-theme',
    autoStart: true,
    optional: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory, _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__.ILauncher, _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_5__.IMainMenu, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette],
    activate: (app, browserFactory, launcher, menu, palette) => {
        const { commands, contextMenu } = app;
        const command = CommandIDs.createNew;
        commands.addCommand(command, {
            label: args => args['isPalette'] || args['isContextMenu']
                ? 'Open Pachyderm Tutorial'
                : 'Pachyderm Tutorial',
            caption: 'Open Pachyderm Tutorial',
            iconClass: args => (args['isPalette'] ? '' : ICON_CLASS),
            execute: async (args) => {
                // const cwd =
                //   args['cwd'] ?? browserFactory?.defaultBrowser.model.path ?? undefined;
                // const model = await commands.execute('docmanager:new-untitled', {
                //   path: cwd,
                //   type: 'file',
                //   ext: 'py'
                // });
                return commands.execute('docmanager:open', {
                    path: "TestNB.ipynb"
                });
            }
        });
        // add to the file browser context menu
        const selectorContent = '.jp-DirListing-content';
        contextMenu.addItem({
            command,
            args: { isContextMenu: true },
            selector: selectorContent,
            rank: 3
        });
        // add to the launcher
        if (launcher) {
            launcher.add({
                command,
                category: 'Notebook',
                rank: 0
            });
        }
        // add to the palette
        if (palette) {
            palette.addItem({
                command,
                args: { isPalette: true },
                category: PALETTE_CATEGORY
            });
        }
        // add to the menu
        if (menu) {
            menu.fileMenu.newMenu.addGroup([{ command }], 30);
        }
    }
};
/**
 * A splash screen for pachyderm
 */
const splash = {
    id: '@pachyderm/jupyterlab-pachyderm-theme:plugin',
    autoStart: true,
    // requires: [ITranslator],
    provides: _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ISplashScreen,
    activate: (app
    // translator: ITranslator
    ) => {
        // const trans = translator.load('jupyterlab');
        const { commands, restored } = app;
        changeFavicon('https://www.pachyderm.com/favicons/favicon.ico');
        const splash = document.createElement('div');
        splash.id = 'pachyderm-splash';
        const logo = document.createElement('div');
        logo.id = 'pachyderm-logo';
        splash.appendChild(logo);
        const graphic = document.createElement('div');
        logo.appendChild(graphic);
        graphic.className = 'logoGraphic';
        const graphicTop = document.createElement('div');
        graphic.appendChild(graphicTop);
        graphicTop.className = 'graphicTop';
        const graphicMid = document.createElement('div');
        graphic.appendChild(graphicMid);
        graphicMid.className = 'graphicMid';
        const graphicBot = document.createElement('div');
        graphic.appendChild(graphicBot);
        graphicBot.className = 'graphicBot';
        const text = document.createElement('div');
        logo.appendChild(text);
        text.className = 'logoText';
        const pachyderm = document.createElement('h1');
        pachyderm.innerHTML = 'Pachyderm';
        text.appendChild(pachyderm);
        const labs = document.createElement('h2');
        labs.innerHTML = 'Notebooks Beta';
        text.appendChild(labs);
        // Create debounced recovery dialog function.
        let dialog;
        const recovery = new _lumino_polling__WEBPACK_IMPORTED_MODULE_1__.Throttler(async () => {
            if (dialog) {
                return;
            }
            dialog = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog({
                title: 'Loading...',
                body: `The loading screen is taking a long time. 
Would you like to clear the workspace or keep waiting?`,
                buttons: [
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.cancelButton({ label: 'Keep Waiting' }),
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.warnButton({ label: 'Clear Workspace' })
                ]
            });
            try {
                const result = await dialog.launch();
                dialog.dispose();
                dialog = null;
                if (result.button.accept && commands.hasCommand(CommandIDs.reset)) {
                    return commands.execute(CommandIDs.reset);
                }
                // Re-invoke the recovery timer in the next frame.
                requestAnimationFrame(() => {
                    // Because recovery can be stopped, handle invocation rejection.
                    void recovery.invoke().catch(_ => undefined);
                });
            }
            catch (error) {
                /* no-op */
            }
        }, { limit: SPLASH_RECOVER_TIMEOUT, edge: 'trailing' });
        // Return ISplashScreen.
        let splashCount = 0;
        return {
            show: () => {
                splash.classList.remove('splash-fade');
                splashCount++;
                console.log('adding');
                document.body.appendChild(splash);
                // Because recovery can be stopped, handle invocation rejection.
                void recovery.invoke().catch(_ => undefined);
                return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_2__.DisposableDelegate(async () => {
                    await restored;
                    if (--splashCount === 0) {
                        void recovery.stop();
                        if (dialog) {
                            dialog.dispose();
                            dialog = null;
                        }
                        splash.classList.add('splash-fade');
                        window.setTimeout(() => {
                            document.body.removeChild(splash);
                        }, 200);
                    }
                });
            }
        };
    },
};
const plugins = [splash, plugin];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
//# sourceMappingURL=index.js.map

/***/ })

}]);
//# sourceMappingURL=lib_index_js-webpack_sharing_consume_default_lumino_coreutils-webpack_sharing_consume_default-afeeb2.155906190fa4ca1f77b3.js.map