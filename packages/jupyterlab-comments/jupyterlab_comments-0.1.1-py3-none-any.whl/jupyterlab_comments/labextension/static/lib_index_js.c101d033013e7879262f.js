"use strict";
(self["webpackChunkjupyterlab_comments"] = self["webpackChunkjupyterlab_comments"] || []).push([["lib_index_js"],{

/***/ "./lib/api/button.js":
/*!***************************!*\
  !*** ./lib/api/button.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NewCommentButton": () => (/* binding */ NewCommentButton)
/* harmony export */ });
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./icons */ "./lib/api/icons.js");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);



class NewCommentButton extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    constructor() {
        super({ node: Private.createNode() });
        this._onClick = () => console.warn('no onClick function registered', this);
        this._closed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
    }
    onAfterAttach(msg) {
        super.onAfterAttach(msg);
        this.node.addEventListener('click', this);
    }
    onAfterDetach(msg) {
        super.onAfterDetach(msg);
        this.node.removeEventListener('click', this);
    }
    handleEvent(event) {
        switch (event.type) {
            case 'click':
                this._handleClick(event);
                break;
        }
    }
    _handleClick(event) {
        event.preventDefault();
        event.stopPropagation();
        this._onClick();
        this.close();
    }
    close() {
        super.close();
        this._closed.emit(undefined);
    }
    open(x, y, f, anchor) {
        // Bail if button is already attached
        // if (this.isAttached) {
        //   return;
        // }
        // Get position/size of main viewport
        const px = window.pageXOffset;
        const py = window.pageYOffset;
        const cw = document.documentElement.clientWidth;
        const ch = document.documentElement.clientHeight;
        let ax = 0;
        let ay = 0;
        if (anchor != null) {
            const { left, top } = anchor.getBoundingClientRect();
            ax = anchor.scrollLeft - left;
            ay = anchor.scrollTop - top;
        }
        // Reset position
        const style = this.node.style;
        style.top = '';
        style.left = '';
        style.visibility = 'hidden';
        if (!this.isAttached) {
            _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget.attach(this, anchor !== null && anchor !== void 0 ? anchor : document.body);
        }
        const { width, height } = this.node.getBoundingClientRect();
        // Constrain button to the viewport
        if (x + width > px + cw) {
            x = px + cw - width;
        }
        if (y + height > py + ch) {
            if (y > py + ch) {
                y = py + ch - height;
            }
            else {
                y = y - height;
            }
        }
        // Adjust according to anchor
        x += ax;
        y += ay;
        // Add onclick function
        this._onClick = f;
        // Update button position and visibility
        style.top = `${Math.max(0, y)}px`;
        style.left = `${Math.max(0, x)}px`;
        style.visibility = '';
    }
    get closed() {
        return this._closed;
    }
}
var Private;
(function (Private) {
    function createNode() {
        const node = document.createElement('div');
        node.className = 'jc-Indicator';
        const icon = _icons__WEBPACK_IMPORTED_MODULE_2__.BlueCreateCommentIcon.element();
        node.appendChild(icon);
        return node;
    }
    Private.createNode = createNode;
})(Private || (Private = {}));


/***/ }),

/***/ "./lib/api/factory.js":
/*!****************************!*\
  !*** ./lib/api/factory.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommentWidgetFactory": () => (/* binding */ CommentWidgetFactory),
/* harmony export */   "CommentFactory": () => (/* binding */ CommentFactory)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./utils */ "./lib/api/utils.js");


class CommentWidgetFactory {
    constructor(options) {
        this.widgetType = '';
        this.commentType = '';
        this.commentRegistry = options.commentRegistry;
    }
    get commentFactory() {
        return this.commentRegistry.getFactory(this.commentType);
    }
}
class CommentFactory {
    constructor() {
        this.type = '';
    }
    createComment(options) {
        const { identity, replies, id, text } = options;
        return {
            text,
            identity,
            type: this.type,
            time: (0,_utils__WEBPACK_IMPORTED_MODULE_1__.getCommentTimeString)(),
            id: id !== null && id !== void 0 ? id : _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.UUID.uuid4(),
            replies: replies !== null && replies !== void 0 ? replies : [],
            target: null
        };
    }
    static createReply(options) {
        const { text, identity, id } = options;
        return {
            text,
            identity,
            id: id !== null && id !== void 0 ? id : _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.UUID.uuid4(),
            time: (0,_utils__WEBPACK_IMPORTED_MODULE_1__.getCommentTimeString)(),
            type: 'reply'
        };
    }
}


/***/ }),

/***/ "./lib/api/header.js":
/*!***************************!*\
  !*** ./lib/api/header.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "PanelHeader": () => (/* binding */ PanelHeader)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./utils */ "./lib/api/utils.js");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);





function FileTitle(props) {
    var _a, _b, _c, _d, _e;
    const panel = props.panel;
    const [isDirty, SetIsDirty] = react__WEBPACK_IMPORTED_MODULE_0__.useState((_b = (_a = panel.model) === null || _a === void 0 ? void 0 : _a.dirty) !== null && _b !== void 0 ? _b : false);
    const [tooltip, SetTooltip] = react__WEBPACK_IMPORTED_MODULE_0__.useState((_d = (_c = panel.fileWidget) === null || _c === void 0 ? void 0 : _c.context.path) !== null && _d !== void 0 ? _d : '');
    const [filename, SetFilename] = react__WEBPACK_IMPORTED_MODULE_0__.useState((_e = panel.sourcePath) !== null && _e !== void 0 ? _e : '');
    const dirtySignalHandler = (_, change) => {
        if (change.name === 'dirty') {
            SetIsDirty(change.newValue);
        }
    };
    const pathChangedHandler = (_, newPath) => {
        var _a, _b, _c;
        SetTooltip((_b = (_a = panel.fileWidget) === null || _a === void 0 ? void 0 : _a.context.path) !== null && _b !== void 0 ? _b : '');
        SetFilename((_c = panel.sourcePath) !== null && _c !== void 0 ? _c : '');
    };
    const modelChangedHandler = (_, widget) => {
        var _a, _b;
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal.disconnectAll(dirtySignalHandler);
        SetTooltip((_a = widget === null || widget === void 0 ? void 0 : widget.context.path) !== null && _a !== void 0 ? _a : '');
        SetFilename((_b = panel.sourcePath) !== null && _b !== void 0 ? _b : '');
        if (widget == null) {
            return;
        }
        const model = widget.context.model;
        model.stateChanged.connect(dirtySignalHandler);
    };
    react__WEBPACK_IMPORTED_MODULE_0__.useEffect(() => {
        panel.modelChanged.connect(modelChangedHandler);
        const fileWidget = panel.fileWidget;
        if (fileWidget != null) {
            fileWidget.context.pathChanged.connect(pathChangedHandler);
        }
        return () => {
            _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal.disconnectAll(modelChangedHandler);
            _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal.disconnectAll(pathChangedHandler);
        };
    });
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { title: tooltip },
        react__WEBPACK_IMPORTED_MODULE_0__.createElement("span", { className: "jc-panelHeader-filename" }, filename),
        isDirty && react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: "jc-DirtyIndicator" })));
}
function UserIdentity(props) {
    const { awareness, panel } = props;
    const handleClick = () => {
        SetEditable(true);
    };
    const [editable, SetEditable] = react__WEBPACK_IMPORTED_MODULE_0__.useState(false);
    const IdentityDiv = () => {
        if (awareness != undefined) {
            return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { contentEditable: editable, className: 'jc-panelHeader-EditInputArea-' + editable, onKeyDown: handleKeydown, suppressContentEditableWarning: true }, (0,_utils__WEBPACK_IMPORTED_MODULE_4__.getIdentity)(awareness).name));
        }
    };
    const handleKeydown = (event) => {
        const target = event.target;
        if (event.key === 'Escape') {
            SetEditable(false);
            target.blur();
            return;
        }
        else if (event.key !== 'Enter') {
            return;
        }
        else if (event.shiftKey) {
            return;
        }
        event.preventDefault();
        event.stopPropagation();
        if (awareness != null) {
            const newName = target.textContent;
            if (newName == null || newName === '') {
                target.textContent = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.getIdentity)(awareness).name;
            }
            else {
                (0,_utils__WEBPACK_IMPORTED_MODULE_4__.setIdentityName)(awareness, newName);
                panel.updateIdentity(awareness.clientID, newName);
            }
        }
        SetEditable(false);
    };
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: "jc-panelHeader-identity-container" },
        IdentityDiv(),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { onClick: () => handleClick() },
            react__WEBPACK_IMPORTED_MODULE_0__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.editIcon.react, { className: "jc-panelHeader-editIcon" }))));
}
class PanelHeader extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ReactWidget {
    constructor(options) {
        super();
        this._renderNeeded = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
        const { panel } = options;
        this._panel = panel;
        this.addClass('jc-panelHeader');
    }
    render() {
        const refresh = () => {
            const fileWidget = this._panel.fileWidget;
            if (fileWidget == null) {
                return;
            }
            fileWidget.initialize();
        };
        const save = () => {
            const fileWidget = this._panel.fileWidget;
            if (fileWidget == null) {
                return;
            }
            void fileWidget.context.save();
            refresh();
        };
        return (react__WEBPACK_IMPORTED_MODULE_0__.createElement(react__WEBPACK_IMPORTED_MODULE_0__.Fragment, null,
            react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: "jc-panelHeader-left" },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.UseSignal, { signal: this._renderNeeded }, () => (react__WEBPACK_IMPORTED_MODULE_0__.createElement(UserIdentity, { awareness: this._awareness, panel: this._panel }))),
                react__WEBPACK_IMPORTED_MODULE_0__.createElement(FileTitle, { panel: this._panel })),
            react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: "jc-panelHeader-right" },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { title: "Save comments", onClick: save, style: { position: 'relative', bottom: '2px' } },
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.saveIcon.react, { className: "jc-Button" })),
                react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { title: "Refresh comments", onClick: refresh },
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.refreshIcon.react, { className: "jc-Button" })))));
    }
    /**
     * A signal emitted when a React re-render is required.
     */
    get renderNeeded() {
        return this._renderNeeded;
    }
    get awareness() {
        return this._awareness;
    }
    set awareness(newValue) {
        this._awareness = newValue;
        this._renderNeeded.emit(undefined);
    }
}


/***/ }),

/***/ "./lib/api/icons.js":
/*!**************************!*\
  !*** ./lib/api/icons.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "randomIcon": () => (/* binding */ randomIcon),
/* harmony export */   "UserIcons": () => (/* binding */ UserIcons),
/* harmony export */   "CommentsHubIcon": () => (/* binding */ CommentsHubIcon),
/* harmony export */   "CommentsPanelIcon": () => (/* binding */ CommentsPanelIcon),
/* harmony export */   "CreateCommentIcon": () => (/* binding */ CreateCommentIcon),
/* harmony export */   "OrangeCreateCommentIcon": () => (/* binding */ OrangeCreateCommentIcon),
/* harmony export */   "BlueCreateCommentIcon": () => (/* binding */ BlueCreateCommentIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _style_icons_user_icon_0_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../style/icons/user-icon-0.svg */ "./style/icons/user-icon-0.svg");
/* harmony import */ var _style_icons_user_icon_1_svg__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../style/icons/user-icon-1.svg */ "./style/icons/user-icon-1.svg");
/* harmony import */ var _style_icons_user_icon_2_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../style/icons/user-icon-2.svg */ "./style/icons/user-icon-2.svg");
/* harmony import */ var _style_icons_user_icon_3_svg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../../style/icons/user-icon-3.svg */ "./style/icons/user-icon-3.svg");
/* harmony import */ var _style_icons_user_icon_4_svg__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../../style/icons/user-icon-4.svg */ "./style/icons/user-icon-4.svg");
/* harmony import */ var _style_icons_user_icon_5_svg__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../../style/icons/user-icon-5.svg */ "./style/icons/user-icon-5.svg");
/* harmony import */ var _style_icons_user_icon_6_svg__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../../style/icons/user-icon-6.svg */ "./style/icons/user-icon-6.svg");
/* harmony import */ var _style_icons_user_icon_7_svg__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../../style/icons/user-icon-7.svg */ "./style/icons/user-icon-7.svg");
/* harmony import */ var _style_icons_user_icon_8_svg__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ../../style/icons/user-icon-8.svg */ "./style/icons/user-icon-8.svg");
/* harmony import */ var _style_icons_user_icon_9_svg__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ../../style/icons/user-icon-9.svg */ "./style/icons/user-icon-9.svg");
/* harmony import */ var _style_icons_user_icon_10_svg__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ../../style/icons/user-icon-10.svg */ "./style/icons/user-icon-10.svg");
/* harmony import */ var _style_icons_user_icon_11_svg__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ../../style/icons/user-icon-11.svg */ "./style/icons/user-icon-11.svg");
/* harmony import */ var _style_icons_user_icon_12_svg__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ../../style/icons/user-icon-12.svg */ "./style/icons/user-icon-12.svg");
/* harmony import */ var _style_icons_user_icon_13_svg__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ../../style/icons/user-icon-13.svg */ "./style/icons/user-icon-13.svg");
/* harmony import */ var _style_icons_user_icon_14_svg__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ../../style/icons/user-icon-14.svg */ "./style/icons/user-icon-14.svg");
/* harmony import */ var _style_icons_user_icon_15_svg__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! ../../style/icons/user-icon-15.svg */ "./style/icons/user-icon-15.svg");
/* harmony import */ var _style_icons_user_icon_16_svg__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ../../style/icons/user-icon-16.svg */ "./style/icons/user-icon-16.svg");
/* harmony import */ var _style_icons_user_icon_17_svg__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! ../../style/icons/user-icon-17.svg */ "./style/icons/user-icon-17.svg");
/* harmony import */ var _style_icons_user_icon_18_svg__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! ../../style/icons/user-icon-18.svg */ "./style/icons/user-icon-18.svg");
/* harmony import */ var _style_icons_user_icon_19_svg__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! ../../style/icons/user-icon-19.svg */ "./style/icons/user-icon-19.svg");
/* harmony import */ var _style_icons_user_icon_20_svg__WEBPACK_IMPORTED_MODULE_21__ = __webpack_require__(/*! ../../style/icons/user-icon-20.svg */ "./style/icons/user-icon-20.svg");
/* harmony import */ var _style_icons_user_icon_21_svg__WEBPACK_IMPORTED_MODULE_22__ = __webpack_require__(/*! ../../style/icons/user-icon-21.svg */ "./style/icons/user-icon-21.svg");
/* harmony import */ var _style_icons_user_icon_22_svg__WEBPACK_IMPORTED_MODULE_23__ = __webpack_require__(/*! ../../style/icons/user-icon-22.svg */ "./style/icons/user-icon-22.svg");
/* harmony import */ var _style_icons_user_icon_23_svg__WEBPACK_IMPORTED_MODULE_24__ = __webpack_require__(/*! ../../style/icons/user-icon-23.svg */ "./style/icons/user-icon-23.svg");

//template
// export const fooIcon = new LabIcon({
//     name: 'barpkg:foo',
//     svgstr: '<svg>...</svg>'
// });
























const userIconSvgstrs = [
    _style_icons_user_icon_0_svg__WEBPACK_IMPORTED_MODULE_1__.default,
    _style_icons_user_icon_1_svg__WEBPACK_IMPORTED_MODULE_2__.default,
    _style_icons_user_icon_2_svg__WEBPACK_IMPORTED_MODULE_3__.default,
    _style_icons_user_icon_3_svg__WEBPACK_IMPORTED_MODULE_4__.default,
    _style_icons_user_icon_4_svg__WEBPACK_IMPORTED_MODULE_5__.default,
    _style_icons_user_icon_5_svg__WEBPACK_IMPORTED_MODULE_6__.default,
    _style_icons_user_icon_6_svg__WEBPACK_IMPORTED_MODULE_7__.default,
    _style_icons_user_icon_7_svg__WEBPACK_IMPORTED_MODULE_8__.default,
    _style_icons_user_icon_8_svg__WEBPACK_IMPORTED_MODULE_9__.default,
    _style_icons_user_icon_9_svg__WEBPACK_IMPORTED_MODULE_10__.default,
    _style_icons_user_icon_10_svg__WEBPACK_IMPORTED_MODULE_11__.default,
    _style_icons_user_icon_11_svg__WEBPACK_IMPORTED_MODULE_12__.default,
    _style_icons_user_icon_12_svg__WEBPACK_IMPORTED_MODULE_13__.default,
    _style_icons_user_icon_13_svg__WEBPACK_IMPORTED_MODULE_14__.default,
    _style_icons_user_icon_14_svg__WEBPACK_IMPORTED_MODULE_15__.default,
    _style_icons_user_icon_15_svg__WEBPACK_IMPORTED_MODULE_16__.default,
    _style_icons_user_icon_16_svg__WEBPACK_IMPORTED_MODULE_17__.default,
    _style_icons_user_icon_17_svg__WEBPACK_IMPORTED_MODULE_18__.default,
    _style_icons_user_icon_18_svg__WEBPACK_IMPORTED_MODULE_19__.default,
    _style_icons_user_icon_19_svg__WEBPACK_IMPORTED_MODULE_20__.default,
    _style_icons_user_icon_20_svg__WEBPACK_IMPORTED_MODULE_21__.default,
    _style_icons_user_icon_21_svg__WEBPACK_IMPORTED_MODULE_22__.default,
    _style_icons_user_icon_22_svg__WEBPACK_IMPORTED_MODULE_23__.default,
    _style_icons_user_icon_23_svg__WEBPACK_IMPORTED_MODULE_24__.default
];
function randomIcon() {
    return UserIcons[Math.floor(Math.random() * UserIcons.length)];
}
const UserIcons = userIconSvgstrs.map((svgstr, index) => {
    return new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
        name: `UserIcon${index}`,
        svgstr
    });
});
const CommentsHubIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'CommentsHubIcon',
    svgstr: `<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="20" height="20" fill="jp-icon2"/>
    <circle cx="10" cy="10" r="9.25" stroke="#616161" stroke-width="1.5"/> 
    <path d="M9.74422 1C6.16412 4 1.15198 11.8 9.74422 19M10.2558 1C13.8359 4 18.848 11.8 10.2558 19" stroke="#616161" stroke-width="1.5"/>  
    <path d="M19 9.84653C16 7.69847 8.2 4.69119 1 9.84653M19 10.1535C16 12.3015 8.2 15.3088 1 10.1535" stroke="#616161" stroke-width="1.5"/> 
    <path d="M10 1V19" stroke="#616161" stroke-width="1.5"/>
  </svg>`
});
const CommentsPanelIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'CommentsPanelIcon',
    svgstr: `<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="18" height="18" fill="none"/>
    <g clip-path="url(#clip0)">
      <path class="jp-icon3" d="M17.25 2.4C17.25 1.96239 17.0762 1.54271 16.7667 1.23327C16.4573 0.923839 16.0376 0.75 15.6 0.75L2.4 0.75C1.96239 0.75 1.54271 0.923839 1.23327 1.23327C0.923839 1.54271 0.75 1.96239 0.75 2.4L0.75 12.3C0.75 12.7376 0.923839 13.1573 1.23327 13.4667C1.54271 13.7762 1.96239 13.95 2.4 13.95H13.95L17.25 17.25V2.4ZM13.95 10.65H4.05V9H13.95V10.65ZM13.95 8.175H4.05V6.525H13.95V8.175ZM13.95 5.7H4.05V4.05H13.95V5.7Z" fill="#616161"/>
      <rect class="jp-icon3" x="0.75" y="12" width="16.5" height="2.25" fill="#616161"/>
      <rect class="jp-icon3" x="0.75" y="0.75" width="16.5" height="2.25" fill="#616161"/>
    </g>
    <defs>
      <clipPath id="clip0">
        <rect class="jp-icon3" width="16.5" height="16.5" fill="white" transform="translate(0.75 0.75)"/>
      </clipPath>
    </defs>
  </svg>`
});
const CreateCommentIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'CreateCommentIcon',
    svgstr: `<svg class="jc-IconShadow" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 18 18" width="18" height="18" style="enable-background:new 0 0 18 18;" xml:space="preserve">
    <path class="jp-icon3" fill="#616161" d="M0,0v14.4h14.4L18,18V0H0z M13.4,7.3H9.6v3.8H8.4V7.3H4.6V6.1h3.8V2.2h1.2v3.8h3.8V7.3z"/>
    <polygon class="jp-icon-accent0" fill="#616161" points="13.4,6.1 13.4,7.3 9.6,7.3 9.6,11.1 8.4,11.1 8.4,7.3 4.6,7.3 4.6,6.1 8.4,6.1 8.4,2.2 9.6,2.2 9.6,6.1 "/>
  </svg>`
});
const OrangeCreateCommentIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'OrangeCreateCommentIcon',
    svgstr: `<svg class="jc-IconShadow" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 18 18" width="18" height="18" style="enable-background:new 0 0 18 18;" xml:space="preserve">
    <path fill="#F57C00" d="M0,0v14.4h14.4L18,18V0H0z M13.4,7.3H9.6v3.8H8.4V7.3H4.6V6.1h3.8V2.2h1.2v3.8h3.8V7.3z"/>
    <polygon class="jp-icon-accent0" fill="#F57C00" points="13.4,6.1 13.4,7.3 9.6,7.3 9.6,11.1 8.4,11.1 8.4,7.3 4.6,7.3 4.6,6.1 8.4,6.1 8.4,2.2 9.6,2.2 9.6,6.1 "/>
  </svg>`
});
const BlueCreateCommentIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'BlueCreateCommentIcon',
    svgstr: `<svg class="jc-IconShadow" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 18 18" width="18" height="18" style="enable-background:new 0 0 18 18;" xml:space="preserve">
    <path fill="#1976D2" d="M0,0v14.4h14.4L18,18V0H0z M13.4,7.3H9.6v3.8H8.4V7.3H4.6V6.1h3.8V2.2h1.2v3.8h3.8V7.3z"/>
    <polygon class="jp-icon-accent0" fill="#1976D2" points="13.4,6.1 13.4,7.3 9.6,7.3 9.6,11.1 8.4,11.1 8.4,7.3 4.6,7.3 4.6,6.1 8.4,6.1 8.4,2.2 9.6,2.2 9.6,6.1 "/>
  </svg>`
});


/***/ }),

/***/ "./lib/api/index.js":
/*!**************************!*\
  !*** ./lib/api/index.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NewCommentButton": () => (/* reexport safe */ _button__WEBPACK_IMPORTED_MODULE_0__.NewCommentButton),
/* harmony export */   "CommentFactory": () => (/* reexport safe */ _factory__WEBPACK_IMPORTED_MODULE_1__.CommentFactory),
/* harmony export */   "CommentWidgetFactory": () => (/* reexport safe */ _factory__WEBPACK_IMPORTED_MODULE_1__.CommentWidgetFactory),
/* harmony export */   "BlueCreateCommentIcon": () => (/* reexport safe */ _icons__WEBPACK_IMPORTED_MODULE_2__.BlueCreateCommentIcon),
/* harmony export */   "CommentsHubIcon": () => (/* reexport safe */ _icons__WEBPACK_IMPORTED_MODULE_2__.CommentsHubIcon),
/* harmony export */   "CommentsPanelIcon": () => (/* reexport safe */ _icons__WEBPACK_IMPORTED_MODULE_2__.CommentsPanelIcon),
/* harmony export */   "CreateCommentIcon": () => (/* reexport safe */ _icons__WEBPACK_IMPORTED_MODULE_2__.CreateCommentIcon),
/* harmony export */   "OrangeCreateCommentIcon": () => (/* reexport safe */ _icons__WEBPACK_IMPORTED_MODULE_2__.OrangeCreateCommentIcon),
/* harmony export */   "UserIcons": () => (/* reexport safe */ _icons__WEBPACK_IMPORTED_MODULE_2__.UserIcons),
/* harmony export */   "randomIcon": () => (/* reexport safe */ _icons__WEBPACK_IMPORTED_MODULE_2__.randomIcon),
/* harmony export */   "CommentFileModel": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_3__.CommentFileModel),
/* harmony export */   "CommentFileModelFactory": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_3__.CommentFileModelFactory),
/* harmony export */   "CommentPanel": () => (/* reexport safe */ _panel__WEBPACK_IMPORTED_MODULE_4__.CommentPanel),
/* harmony export */   "commentRegistryPlugin": () => (/* reexport safe */ _plugin__WEBPACK_IMPORTED_MODULE_5__.commentRegistryPlugin),
/* harmony export */   "commentWidgetRegistryPlugin": () => (/* reexport safe */ _plugin__WEBPACK_IMPORTED_MODULE_5__.commentWidgetRegistryPlugin),
/* harmony export */   "jupyterCommentingPlugin": () => (/* reexport safe */ _plugin__WEBPACK_IMPORTED_MODULE_5__.jupyterCommentingPlugin),
/* harmony export */   "PanelHeader": () => (/* reexport safe */ _header__WEBPACK_IMPORTED_MODULE_6__.PanelHeader),
/* harmony export */   "CommentRegistry": () => (/* reexport safe */ _registry__WEBPACK_IMPORTED_MODULE_7__.CommentRegistry),
/* harmony export */   "CommentWidgetRegistry": () => (/* reexport safe */ _registry__WEBPACK_IMPORTED_MODULE_7__.CommentWidgetRegistry),
/* harmony export */   "emptyIdentity": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.emptyIdentity),
/* harmony export */   "getCommentTimeString": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.getCommentTimeString),
/* harmony export */   "getIdentity": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.getIdentity),
/* harmony export */   "hashString": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.hashString),
/* harmony export */   "lineToIndex": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.lineToIndex),
/* harmony export */   "randomColor": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.randomColor),
/* harmony export */   "randomIdentity": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.randomIdentity),
/* harmony export */   "setIdentityName": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.setIdentityName),
/* harmony export */   "toCodeEditorPosition": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.toCodeEditorPosition),
/* harmony export */   "toCodeMirrorPosition": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.toCodeMirrorPosition),
/* harmony export */   "truncate": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_8__.truncate),
/* harmony export */   "ICommentPanel": () => (/* reexport safe */ _token__WEBPACK_IMPORTED_MODULE_9__.ICommentPanel),
/* harmony export */   "ICommentRegistry": () => (/* reexport safe */ _token__WEBPACK_IMPORTED_MODULE_9__.ICommentRegistry),
/* harmony export */   "ICommentWidgetRegistry": () => (/* reexport safe */ _token__WEBPACK_IMPORTED_MODULE_9__.ICommentWidgetRegistry),
/* harmony export */   "CommentFileWidget": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_10__.CommentFileWidget),
/* harmony export */   "CommentWidget": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_10__.CommentWidget)
/* harmony export */ });
/* harmony import */ var _button__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./button */ "./lib/api/button.js");
/* harmony import */ var _factory__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./factory */ "./lib/api/factory.js");
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./icons */ "./lib/api/icons.js");
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./model */ "./lib/api/model.js");
/* harmony import */ var _panel__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./panel */ "./lib/api/panel.js");
/* harmony import */ var _plugin__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./plugin */ "./lib/api/plugin.js");
/* harmony import */ var _header__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./header */ "./lib/api/header.js");
/* harmony import */ var _registry__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./registry */ "./lib/api/registry.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./utils */ "./lib/api/utils.js");
/* harmony import */ var _token__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./token */ "./lib/api/token.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./widget */ "./lib/api/widget.js");














/***/ }),

/***/ "./lib/api/model.js":
/*!**************************!*\
  !*** ./lib/api/model.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommentFileModel": () => (/* binding */ CommentFileModel),
/* harmony export */   "CommentFileModelFactory": () => (/* binding */ CommentFileModelFactory)
/* harmony export */ });
/* harmony import */ var _factory__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./factory */ "./lib/api/factory.js");
/* harmony import */ var _jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/shared-models */ "webpack/sharing/consume/default/@jupyterlab/shared-models");
/* harmony import */ var _jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/observables */ "webpack/sharing/consume/default/@jupyterlab/observables");
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_observables__WEBPACK_IMPORTED_MODULE_2__);




/**
 * The default model for comment files.
 */
class CommentFileModel {
    /**
     * Construct a new `CommentFileModel`.
     */
    constructor(options) {
        this._commentsObserver = (events) => {
            for (let event of events) {
                const delta = event.delta;
                // Converts a deletion followed by an insertion into an update
                // Normally, yjs doesn't propagate changes to the contents of a YArray,
                // only insertions and deletions.
                // Parsing a deletion/insertion pair into an update allows clients to
                // communicate when a comment has been changed over yjs.
                let lastInserted = 0;
                for (let i = 0; i < delta.length; i++) {
                    let d = delta[i];
                    if (d.insert != null) {
                        lastInserted = d.insert.length;
                    }
                    else if (d.delete != null) {
                        if (lastInserted === d.delete) {
                            delta.splice(i - 1, 2, { update: lastInserted });
                        }
                        lastInserted = 0;
                    }
                    else {
                        lastInserted = 0;
                    }
                }
                this._changed.emit(delta);
            }
        };
        /**
         * The underlying model handling RTC between clients.
         */
        this.ymodel = new _jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_0__.YDocument();
        // These are never used--just here to satisfy the interface requirements.
        this.modelDB = new _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_2__.ModelDB();
        this.defaultKernelLanguage = '';
        this.defaultKernelName = '';
        this._dirty = false;
        this._readOnly = false;
        this._isDisposed = false;
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._stateChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._contentChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        const { commentRegistry, commentWidgetRegistry, commentMenu, isInitialized } = options;
        this.commentRegistry = commentRegistry;
        this.commentWidgetRegistry = commentWidgetRegistry;
        this._commentMenu = commentMenu;
        this._isInitialized = isInitialized !== null && isInitialized !== void 0 ? isInitialized : false;
        this.comments.observeDeep(this._commentsObserver);
    }
    /**
     * Dispose of the model and its resources.
     */
    dispose() {
        if (this._isDisposed) {
            return;
        }
        this._isDisposed = true;
        this.comments.unobserveDeep(this._commentsObserver);
    }
    /**
     * Serialize the model to JSON.
     */
    toJSON() {
        if (this.widgets == null) {
            console.warn('No comment widgets found for model. Serializing based on default IComment');
            return this.comments.toJSON();
        }
        return this.widgets.map(widget => widget.toJSON());
    }
    /**
     * Deserialize the model from JSON.
     */
    fromJSON(value) {
        this.ymodel.transact(() => {
            const comments = this.comments;
            comments.delete(0, comments.length);
            comments.push(value);
        });
        this._signalContentChange();
    }
    /**
     * Serialize the model to a string.
     */
    toString() {
        return JSON.stringify(this.toJSON(), undefined, 2);
    }
    /**
     * Deserialize the model from a string.
     */
    fromString(value) {
        this.fromJSON(JSON.parse(value !== '' ? value : '[]'));
    }
    _updateComment(comment, index) {
        const comments = this.comments;
        this.ymodel.ydoc.transact(() => {
            comments.delete(index);
            comments.insert(index, [comment]);
        });
        this._signalContentChange();
    }
    /**
     * Create a comment from an `ICommentOptions` object.
     *
     * ### Notes
     * This will fail if there's no factory for the given comment type.
     */
    createComment(options) {
        const factory = this.commentRegistry.getFactory(options.type);
        if (factory == null) {
            return;
        }
        return factory.createComment(options);
    }
    /**
     * Create a reply from an `IReplyOptions` object.
     */
    createReply(options) {
        return _factory__WEBPACK_IMPORTED_MODULE_3__.CommentFactory.createReply(options);
    }
    /**
     * Create a comment from `options` and inserts it in `this.comments` at `index`.
     */
    insertComment(options, index) {
        const comment = this.createComment(options);
        if (comment == null) {
            return;
        }
        this.comments.insert(index, [comment]);
        // Delta emitted by listener
        this._signalContentChange();
    }
    /**
     * Creates a comment from `options` and inserts it at the end of `this.comments`.
     */
    addComment(options) {
        const comment = this.createComment(options);
        if (comment == null) {
            return;
        }
        this.comments.push([comment]);
        // Delta emitted by listener
        this._signalContentChange();
    }
    /**
     * Creates a reply from `options` and inserts it in the replies of the comment
     * with id `parentID` at `index`.
     */
    insertReply(options, parentID, index) {
        const loc = this.getComment(parentID);
        if (loc == null) {
            return;
        }
        const reply = this.createReply(options);
        const newComment = Object.assign({}, loc.comment);
        newComment.replies.splice(index, 0, reply);
        this._updateComment(newComment, loc.index);
    }
    /**
     * Creates a reply from `options` and appends it to the replies of the comment
     * with id `parentID`.
     */
    addReply(options, parentID) {
        const loc = this.getComment(parentID);
        if (loc == null) {
            return;
        }
        const reply = this.createReply(options);
        const newComment = Object.assign({}, loc.comment);
        newComment.replies.push(reply);
        this._updateComment(newComment, loc.index);
    }
    /**
     * Deletes the comment with id `id` from `this.comments`.
     */
    deleteComment(id) {
        const loc = this.getComment(id);
        if (loc == null) {
            return;
        }
        this.comments.delete(loc.index);
        // Delta emitted by listener
        this._signalContentChange();
    }
    /**
     * Deletes the reply with id `id` from `this.comments`.
     *
     * If a `parentID` is given, it will be used to locate the parent comment.
     * Otherwise, all comments will be searched for the reply with the given id.
     */
    deleteReply(id, parentID) {
        const loc = this.getReply(id, parentID);
        if (loc == null) {
            return;
        }
        const newComment = Object.assign({}, loc.parent);
        newComment.replies.splice(loc.index, 1);
        this._updateComment(newComment, loc.parentIndex);
    }
    /**
     * Applies the changes in `options` to the comment with id `id`.
     */
    editComment(options, id) {
        const loc = this.getComment(id);
        if (loc == null) {
            return;
        }
        const newComment = Object.assign(Object.assign({}, loc.comment), options);
        this._updateComment(newComment, loc.index);
    }
    /**
     * Applies the changes in `options` to the reply with id `id`.
     *
     * If a `parentID` is given, it will be used to locate the parent comment.
     * Otherwise, all comments will be searched for the reply with the given id.
     */
    editReply(options, id, parentID) {
        const loc = this.getReply(id, parentID);
        if (loc == null) {
            return;
        }
        Object.assign(loc.reply, loc.reply, options);
        const newComment = Object.assign({}, loc.parent);
        this._updateComment(newComment, loc.parentIndex);
    }
    /**
     * Get the comment with id `id`. Returns undefined if not found.
     */
    getComment(id) {
        const comments = this.comments;
        for (let i = 0; i < comments.length; i++) {
            const comment = comments.get(i);
            if (comment.id === id) {
                return {
                    index: i,
                    comment
                };
            }
        }
        return;
    }
    /**
     * Returns the reply with id `id`. Returns undefined if not found.
     *
     * If a `parentID` is given, it will be used to locate the parent comment.
     * Otherwise, all comments will be searched for the reply with the given id.
     */
    getReply(id, parentID) {
        let parentIndex;
        let parent;
        if (parentID != null) {
            const parentLocation = this.getComment(parentID);
            if (parentLocation == null) {
                return;
            }
            parentIndex = parentLocation.index;
            parent = parentLocation.comment;
            for (let i = 0; i < parent.replies.length; i++) {
                const reply = parent.replies[i];
                if (reply.id === id) {
                    return {
                        parentIndex,
                        parent,
                        reply,
                        index: i
                    };
                }
            }
            return;
        }
        const comments = this.comments;
        for (let i = 0; i < comments.length; i++) {
            const parent = comments.get(i);
            for (let j = 0; i < parent.replies.length; i++) {
                const reply = parent.replies[j];
                if (reply.id === id) {
                    return {
                        parentIndex: i,
                        parent,
                        reply,
                        index: j
                    };
                }
            }
        }
        return;
    }
    initialize() {
        this.sharedModel.clearUndoHistory();
        this._isInitialized = true;
    }
    /**
     * The comments associated with the model.
     */
    get comments() {
        return this.ymodel.ydoc.getArray('comments');
    }
    /**
     * The awareness associated with the document being commented on.
     */
    get awareness() {
        return this.ymodel.awareness;
    }
    /**
     * The dropdown menu for comment widgets.
     */
    get commentMenu() {
        return this._commentMenu;
    }
    /**
     * TODO: A signal emitted when the model is changed.
     * See the notes on `CommentFileModel.IChange` below.
     */
    get changed() {
        return this._changed;
    }
    get sharedModel() {
        return this.ymodel;
    }
    get readOnly() {
        return this._readOnly;
    }
    set readOnly(newVal) {
        const oldVal = this.readOnly;
        if (newVal !== oldVal) {
            this._readOnly = newVal;
            this._signalStateChange(oldVal, newVal, 'readOnly');
        }
    }
    get dirty() {
        return this._dirty;
    }
    set dirty(newVal) {
        const oldVal = this.dirty;
        if (newVal !== oldVal) {
            this._dirty = newVal;
            this._signalStateChange(oldVal, newVal, 'dirty');
        }
    }
    get stateChanged() {
        return this._stateChanged;
    }
    get contentChanged() {
        return this._contentChanged;
    }
    get isDisposed() {
        return this._isDisposed;
    }
    get isInitialized() {
        return this._isInitialized;
    }
    _signalStateChange(oldValue, newValue, name) {
        this._stateChanged.emit({
            oldValue,
            newValue,
            name
        });
    }
    _signalContentChange() {
        this.dirty = true;
        this._contentChanged.emit();
    }
}
class CommentFileModelFactory {
    constructor(options) {
        this.name = 'comment-file';
        this.contentType = 'file';
        this.fileFormat = 'text';
        this._isDisposed = false;
        const { commentRegistry, commentWidgetRegistry, commentMenu } = options;
        this._commentRegistry = commentRegistry;
        this._commentWidgetRegistry = commentWidgetRegistry;
        this._commentMenu = commentMenu;
    }
    createNew(languagePreference, modelDB, isInitialized) {
        const commentRegistry = this._commentRegistry;
        const commentWidgetRegistry = this._commentWidgetRegistry;
        const commentMenu = this._commentMenu;
        return new CommentFileModel({
            commentRegistry,
            commentWidgetRegistry,
            commentMenu,
            isInitialized
        });
    }
    preferredLanguage(path) {
        return '';
    }
    dispose() {
        this._isDisposed = true;
    }
    get isDisposed() {
        return this._isDisposed;
    }
}


/***/ }),

/***/ "./lib/api/panel.js":
/*!**************************!*\
  !*** ./lib/api/panel.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommentPanel": () => (/* binding */ CommentPanel)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./widget */ "./lib/api/widget.js");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _header__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./header */ "./lib/api/header.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./utils */ "./lib/api/utils.js");
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./icons */ "./lib/api/icons.js");
/* harmony import */ var _button__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./button */ "./lib/api/button.js");








class CommentPanel extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Panel {
    constructor(options) {
        super();
        this._commentAdded = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._revealed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._fileWidget = undefined;
        this._modelChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._pathPrefix = 'comments/';
        this._button = new _button__WEBPACK_IMPORTED_MODULE_3__.NewCommentButton();
        this._loadingModel = false;
        this._sourcePath = null;
        this.id = `CommentPanel-${_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.UUID.uuid4()}`;
        this.title.icon = _icons__WEBPACK_IMPORTED_MODULE_4__.CommentsPanelIcon;
        this.addClass('jc-CommentPanel');
        const { docManager, commentRegistry, commentWidgetRegistry, shell, renderer } = options;
        this._commentRegistry = commentRegistry;
        this._commentWidgetRegistry = commentWidgetRegistry;
        this._commentMenu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Menu({ commands: options.commands });
        this._docManager = docManager;
        const panelHeader = new _header__WEBPACK_IMPORTED_MODULE_5__.PanelHeader({
            shell,
            panel: this
        });
        this.addWidget(panelHeader);
        this._panelHeader = panelHeader;
        this.renderer = renderer;
        this._localIdentity = (0,_utils__WEBPACK_IMPORTED_MODULE_6__.randomIdentity)();
        const urlSearchParams = new URLSearchParams(window.location.search);
        const urlName = urlSearchParams.get('name');
        if (urlName != null) {
            this._localIdentity.name = urlName;
        }
        docManager.services.contents.fileChanged.connect(this._onFileChange, this);
    }
    async _onFileChange(contents, change) {
        var _a;
        const sourcePath = (_a = change === null || change === void 0 ? void 0 : change.oldValue) === null || _a === void 0 ? void 0 : _a.path;
        const commentsPath = sourcePath != null ? this.getCommentPathFor(sourcePath) : undefined;
        switch (change.type) {
            case 'delete':
                if (await this.pathExists(commentsPath)) {
                    return contents.delete(commentsPath);
                }
                break;
            case 'rename':
                const newPath = change.newValue.path;
                if (!(await this.pathExists(commentsPath))) {
                    return;
                }
                const newCommentsPath = this.getCommentPathFor(newPath);
                if (this.sourcePath === sourcePath) {
                    this._sourcePath = newPath;
                }
                return void contents.rename(commentsPath, newCommentsPath);
            case 'save':
                if (this.sourcePath === change.newValue.path) {
                    return this._fileWidget.context.save();
                }
                break;
        }
    }
    getCommentFileNameFor(sourcePath) {
        return (0,_utils__WEBPACK_IMPORTED_MODULE_6__.hashString)(sourcePath).toString() + '.comment';
    }
    getCommentPathFor(sourcePath) {
        return this.pathPrefix + this.getCommentFileNameFor(sourcePath);
    }
    onUpdateRequest(msg) {
        if (this._fileWidget == null) {
            return;
        }
        const awareness = this.awareness;
        if (awareness != null && awareness !== this.panelHeader.awareness) {
            this.panelHeader.awareness = awareness;
        }
    }
    pathExists(path) {
        const contents = this._docManager.services.contents;
        return contents
            .get(path, { content: false })
            .then(() => true)
            .catch(() => false);
    }
    async getContext(path) {
        var _a;
        const docManager = this._docManager;
        const factory = docManager.registry.getModelFactory('comment-file');
        const preference = docManager.registry.getKernelPreference(path, 'comment-factory');
        const context = (_a = 
        // @ts-ignore
        docManager._findContext(path, 'comment-file')) !== null && _a !== void 0 ? _a : 
        // @ts-ignore
        docManager._createContext(path, factory, preference);
        await docManager.services.ready;
        const exists = await this.pathExists(path);
        void context.initialize(!exists);
        return context;
    }
    async loadModel(context) {
        // Lock to prevent multiple loads at the same time.
        if (this._loadingModel) {
            return;
        }
        const sourcePath = context.path;
        // Attempting to load model for a non-document widget
        if (sourcePath === '' ||
            (this._sourcePath && this._sourcePath === sourcePath)) {
            return;
        }
        this._sourcePath = sourcePath;
        this._loadingModel = true;
        if (this._fileWidget != null) {
            this.model.changed.disconnect(this._onChange, this);
            const oldWidget = this._fileWidget;
            oldWidget.hide();
            if (!oldWidget.context.isDisposed) {
                await oldWidget.context.save();
                oldWidget.dispose();
            }
        }
        const path = this.getCommentPathFor(sourcePath);
        const commentContext = await this.getContext(path);
        await commentContext.ready;
        const content = new _widget__WEBPACK_IMPORTED_MODULE_7__.CommentFileWidget({ context: commentContext }, this.renderer);
        this._fileWidget = content;
        this.addWidget(content);
        content.commentAdded.connect((_, widget) => this._commentAdded.emit(widget));
        this.model.changed.connect(this._onChange, this);
        const { name, color, icon } = this._localIdentity;
        this.model.awareness.setLocalStateField('user', {
            name,
            color,
            icon
        });
        this.update();
        content.initialize();
        this._modelChanged.emit(content);
        this._loadingModel = false;
    }
    _onChange(_, changes) {
        const fileWidget = this.fileWidget;
        if (fileWidget == null) {
            return;
        }
        const widgets = fileWidget.widgets;
        let index = 0;
        for (let change of changes) {
            if (change.retain != null) {
                index += change.retain;
            }
            else if (change.insert != null) {
                change.insert.forEach(comment => fileWidget.insertComment(comment, index++));
            }
            else if (change.delete != null) {
                widgets
                    .slice(index, index + change.delete)
                    .forEach(widget => widget.dispose());
            }
            else if (change.update != null) {
                for (let i = 0; i < change.update; i++) {
                    widgets[index++].update();
                }
            }
        }
    }
    get ymodel() {
        if (this._fileWidget == null) {
            return;
        }
        return this._fileWidget.context.model.sharedModel;
    }
    get model() {
        const docWidget = this._fileWidget;
        if (docWidget == null) {
            return;
        }
        return docWidget.model;
    }
    get fileWidget() {
        return this._fileWidget;
    }
    get modelChanged() {
        return this._modelChanged;
    }
    /**
     * Scroll the comment with the given id into view.
     */
    scrollToComment(id) {
        const node = document.getElementById(id);
        if (node == null) {
            return;
        }
        node.scrollIntoView({ behavior: 'smooth' });
    }
    /**
     * Show the widget, make it visible to its parent widget, and emit the
     * `revealed` signal.
     *
     * ### Notes
     * This causes the [[isHidden]] property to be false.
     * If the widget is not explicitly hidden, this is a no-op.
     */
    show() {
        if (this.isHidden) {
            this._revealed.emit(undefined);
            super.show();
        }
    }
    /**
     * A signal emitted when a comment is added to the panel.
     */
    get commentAdded() {
        return this._commentAdded;
    }
    /**
     * The dropdown menu for comment widgets.
     */
    get commentMenu() {
        return this._commentMenu;
    }
    /**
     * A signal emitted when the panel is about to be shown.
     */
    get revealed() {
        return this._revealed;
    }
    get panelHeader() {
        return this._panelHeader;
    }
    get awareness() {
        var _a;
        return (_a = this.model) === null || _a === void 0 ? void 0 : _a.awareness;
    }
    get commentRegistry() {
        return this._commentRegistry;
    }
    get commentWidgetRegistry() {
        return this._commentWidgetRegistry;
    }
    get pathPrefix() {
        return this._pathPrefix;
    }
    set pathPrefix(newValue) {
        this._pathPrefix = newValue;
    }
    get sourcePath() {
        return this._sourcePath;
    }
    mockComment(options, index) {
        const model = this.model;
        if (model == null) {
            return;
        }
        const commentFactory = this.commentRegistry.getFactory(options.type);
        if (commentFactory == null) {
            return;
        }
        const comment = commentFactory.createComment(Object.assign(Object.assign({}, options), { text: '' }));
        const widgetFactory = this.commentWidgetRegistry.getFactory(options.type);
        if (widgetFactory == null) {
            return;
        }
        const widget = widgetFactory.createWidget(comment, model, options.source);
        if (widget == null) {
            return;
        }
        widget.isMock = true;
        this.fileWidget.insertWidget(index, widget);
        this._commentAdded.emit(widget);
    }
    updateIdentity(id, newName) {
        this._localIdentity.name = newName;
        const model = this.model;
        if (model == null) {
            return;
        }
        model.comments.forEach(comment => {
            if (comment.identity.id === id) {
                model.editComment({
                    identity: Object.assign(Object.assign({}, comment.identity), { name: newName })
                }, comment.id);
            }
            comment.replies.forEach(reply => {
                if (reply.identity.id === id) {
                    model.editReply({
                        identity: Object.assign(Object.assign({}, reply.identity), { name: newName })
                    }, reply.id, comment.id);
                }
            });
        });
        this.update();
    }
    get button() {
        return this._button;
    }
    get localIdentity() {
        return this._localIdentity;
    }
}


/***/ }),

/***/ "./lib/api/plugin.js":
/*!***************************!*\
  !*** ./lib/api/plugin.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "commentRegistryPlugin": () => (/* binding */ commentRegistryPlugin),
/* harmony export */   "commentWidgetRegistryPlugin": () => (/* binding */ commentWidgetRegistryPlugin),
/* harmony export */   "jupyterCommentingPlugin": () => (/* binding */ jupyterCommentingPlugin),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _panel__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./panel */ "./lib/api/panel.js");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _registry__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./registry */ "./lib/api/registry.js");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./model */ "./lib/api/model.js");
/* harmony import */ var _token__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./token */ "./lib/api/token.js");










var CommandIDs;
(function (CommandIDs) {
    CommandIDs.addComment = 'jl-comments:add-comment';
    CommandIDs.deleteComment = 'jl-comments:delete-comment';
    CommandIDs.editComment = 'jl-comments:edit-comment';
    CommandIDs.replyToComment = 'jl-comments:reply-to-comment';
    CommandIDs.save = 'jl-comments:save';
})(CommandIDs || (CommandIDs = {}));
/**
 * A plugin that provides a `CommentRegistry`
 */
const commentRegistryPlugin = {
    id: 'jupyterlab-comments:comment-registry',
    autoStart: true,
    provides: _token__WEBPACK_IMPORTED_MODULE_6__.ICommentRegistry,
    activate: (app) => {
        return new _registry__WEBPACK_IMPORTED_MODULE_7__.CommentRegistry();
    }
};
/**
 * A plugin that provides a `CommentWidgetRegistry`
 */
const commentWidgetRegistryPlugin = {
    id: 'jupyterlab-comments:comment-widget-registry',
    autoStart: true,
    provides: _token__WEBPACK_IMPORTED_MODULE_6__.ICommentWidgetRegistry,
    activate: (app) => {
        return new _registry__WEBPACK_IMPORTED_MODULE_7__.CommentWidgetRegistry();
    }
};
const jupyterCommentingPlugin = {
    id: 'jupyterlab-comments:commenting-api',
    autoStart: true,
    requires: [
        _token__WEBPACK_IMPORTED_MODULE_6__.ICommentRegistry,
        _token__WEBPACK_IMPORTED_MODULE_6__.ICommentWidgetRegistry,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell,
        _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager,
        _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.IRenderMimeRegistry
    ],
    provides: _token__WEBPACK_IMPORTED_MODULE_6__.ICommentPanel,
    activate: (app, commentRegistry, commentWidgetRegistry, shell, docManager, renderer) => {
        const filetype = {
            contentType: 'file',
            displayName: 'comment',
            extensions: ['.comment'],
            fileFormat: 'json',
            name: 'comment',
            mimeTypes: ['application/json']
        };
        const commentTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: 'comment-widgets'
        });
        const panel = new _panel__WEBPACK_IMPORTED_MODULE_8__.CommentPanel({
            commands: app.commands,
            commentRegistry,
            commentWidgetRegistry,
            docManager,
            shell,
            renderer
        });
        // Create the directory holding the comments.
        void panel.pathExists(panel.pathPrefix).then(exists => {
            const contents = docManager.services.contents;
            if (!exists) {
                void contents
                    .newUntitled({
                    path: '/',
                    type: 'directory'
                })
                    .then(model => {
                    void contents.rename(model.path, panel.pathPrefix);
                });
            }
        });
        addCommands(app, commentTracker, panel);
        const commentMenu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.Menu({ commands: app.commands });
        commentMenu.addItem({ command: CommandIDs.deleteComment });
        commentMenu.addItem({ command: CommandIDs.editComment });
        commentMenu.addItem({ command: CommandIDs.replyToComment });
        app.contextMenu.addItem({
            command: CommandIDs.deleteComment,
            selector: '.jc-Comment'
        });
        app.contextMenu.addItem({
            command: CommandIDs.editComment,
            selector: '.jc-Comment'
        });
        app.contextMenu.addItem({
            command: CommandIDs.replyToComment,
            selector: '.jc-Comment'
        });
        const modelFactory = new _model__WEBPACK_IMPORTED_MODULE_9__.CommentFileModelFactory({
            commentRegistry,
            commentWidgetRegistry,
            commentMenu
        });
        app.docRegistry.addFileType(filetype);
        app.docRegistry.addModelFactory(modelFactory);
        // Add the panel to the shell's right area.
        shell.add(panel, 'right', { rank: 600 });
        // Load model for current document when it changes
        shell.currentChanged.connect((_, args) => {
            if (args.newValue != null && args.newValue instanceof _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_4__.DocumentWidget) {
                const docWidget = args.newValue;
                docWidget.context.ready
                    .then(() => {
                    void panel.loadModel(docWidget.context);
                })
                    .catch(() => {
                    console.warn('Unable to load panel');
                });
            }
        });
        // Update comment widget tracker when model changes
        panel.modelChanged.connect((_, fileWidget) => {
            if (fileWidget != null) {
                fileWidget.widgets.forEach(widget => void commentTracker.add(widget));
                fileWidget.commentAdded.connect((_, commentWidget) => void commentTracker.add(commentWidget));
            }
        });
        // Reveal the comment panel when a comment is added.
        panel.commentAdded.connect((_, comment) => {
            const identity = comment.identity;
            // If you didn't make the comment, ignore it
            // Comparing ids would be better but they're not synchronized across Docs/awarenesses
            if (identity == null || identity.name !== panel.localIdentity.name) {
                return;
            }
            // Automatically opens panel when a document with comments is opened,
            // or when the local user adds a new comment
            if (!panel.isVisible) {
                shell.activateById(panel.id);
                if (comment.text === '') {
                    comment.openEditActive();
                }
            }
            panel.scrollToComment(comment.id);
        });
        app.contextMenu.addItem({
            command: CommandIDs.save,
            selector: '.jc-CommentPanel'
        });
        return panel;
    }
};
function addCommands(app, commentTracker, panel) {
    app.commands.addCommand(CommandIDs.save, {
        label: 'Save Comments',
        execute: () => {
            const fileWidget = panel.fileWidget;
            if (fileWidget == null) {
                return;
            }
            void fileWidget.context.save();
        }
    });
    app.commands.addCommand(CommandIDs.deleteComment, {
        label: 'Delete Comment',
        execute: () => {
            const currentComment = commentTracker.currentWidget;
            if (currentComment != null) {
                currentComment.deleteActive();
            }
        }
    });
    app.commands.addCommand(CommandIDs.editComment, {
        label: 'Edit Comment',
        execute: () => {
            const currentComment = commentTracker.currentWidget;
            if (currentComment != null) {
                currentComment.openEditActive();
            }
        }
    });
    app.commands.addCommand(CommandIDs.replyToComment, {
        label: 'Reply to Comment',
        execute: () => {
            const currentComment = commentTracker.currentWidget;
            if (currentComment != null) {
                currentComment.revealReply();
            }
        }
    });
}
const plugins = [
    jupyterCommentingPlugin,
    commentRegistryPlugin,
    commentWidgetRegistryPlugin
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "./lib/api/registry.js":
/*!*****************************!*\
  !*** ./lib/api/registry.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommentRegistry": () => (/* binding */ CommentRegistry),
/* harmony export */   "CommentWidgetRegistry": () => (/* binding */ CommentWidgetRegistry)
/* harmony export */ });
/**
 * A class that manages a map of `CommentFactory`s
 */
class CommentRegistry {
    constructor() {
        this.factories = new Map();
    }
    addFactory(factory) {
        this.factories.set(factory.type, factory);
    }
    getFactory(type) {
        return this.factories.get(type);
    }
}
/**
 * A class that manages a map of `CommentWidgetFactory`s
 */
class CommentWidgetRegistry {
    constructor() {
        this.factories = new Map();
    }
    addFactory(factory) {
        this.factories.set(factory.widgetType, factory);
    }
    getFactory(type) {
        return this.factories.get(type);
    }
}


/***/ }),

/***/ "./lib/api/token.js":
/*!**************************!*\
  !*** ./lib/api/token.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ICommentRegistry": () => (/* binding */ ICommentRegistry),
/* harmony export */   "ICommentWidgetRegistry": () => (/* binding */ ICommentWidgetRegistry),
/* harmony export */   "ICommentPanel": () => (/* binding */ ICommentPanel)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);

const ICommentRegistry = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('jupyterlab-comments:comment-registry');
const ICommentWidgetRegistry = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('jupyterlab-comment:comment-widget-registry');
const ICommentPanel = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('jupyterlab-comments:comment-panel');


/***/ }),

/***/ "./lib/api/utils.js":
/*!**************************!*\
  !*** ./lib/api/utils.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "emptyIdentity": () => (/* binding */ emptyIdentity),
/* harmony export */   "randomIdentity": () => (/* binding */ randomIdentity),
/* harmony export */   "randomColor": () => (/* binding */ randomColor),
/* harmony export */   "setIdentityName": () => (/* binding */ setIdentityName),
/* harmony export */   "getIdentity": () => (/* binding */ getIdentity),
/* harmony export */   "getCommentTimeString": () => (/* binding */ getCommentTimeString),
/* harmony export */   "lineToIndex": () => (/* binding */ lineToIndex),
/* harmony export */   "hashString": () => (/* binding */ hashString),
/* harmony export */   "truncate": () => (/* binding */ truncate),
/* harmony export */   "toCodeMirrorPosition": () => (/* binding */ toCodeMirrorPosition),
/* harmony export */   "toCodeEditorPosition": () => (/* binding */ toCodeEditorPosition)
/* harmony export */ });
/* harmony import */ var _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/docprovider */ "webpack/sharing/consume/default/@jupyterlab/docprovider");
/* harmony import */ var _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./icons */ "./lib/api/icons.js");


const emptyIdentity = {
    id: 0,
    icon: 0,
    name: 'User',
    color: ''
};
let count = -1;
function randomIdentity() {
    return {
        id: count--,
        name: (0,_jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_0__.getAnonymousUserName)(),
        color: randomColor(),
        icon: Math.floor(Math.random() * _icons__WEBPACK_IMPORTED_MODULE_1__.UserIcons.length)
    };
}
function randomColor() {
    const validColors = [
        '#eb5351',
        '#ea357a',
        '#f57c00',
        '#dca927',
        '#24be61',
        '#8ed97c',
        '#ff709b',
        '#d170ff',
        '#7b61ff',
        '#4176ff',
        '#70c3ff',
        '#a8b84a'
    ];
    return validColors[Math.floor(Math.random() * validColors.length)];
}
function setIdentityName(awareness, name) {
    var _a;
    let localState = awareness.getLocalState();
    if (localState == null) {
        return false;
    }
    const oldUser = localState['user'];
    if (oldUser == null) {
        return false;
    }
    let newUser = {
        name: name,
        color: oldUser['color'],
        icon: (_a = oldUser['icon']) !== null && _a !== void 0 ? _a : Math.floor(Math.random() * _icons__WEBPACK_IMPORTED_MODULE_1__.UserIcons.length)
    };
    awareness.setLocalStateField('user', newUser);
    //Checking if the localState has been updated
    localState = awareness.getLocalState();
    if (localState == null) {
        return false;
    }
    if (localState['user']['name'] != name) {
        return false;
    }
    return true;
}
function getIdentity(awareness) {
    const localState = awareness.getLocalState();
    if (localState == null) {
        return emptyIdentity;
    }
    const userInfo = localState['user'];
    if (userInfo != null &&
        'name' in userInfo &&
        'color' in userInfo &&
        'icon' in userInfo) {
        return {
            id: awareness.clientID,
            name: userInfo['name'],
            color: userInfo['color'],
            icon: userInfo['icon']
        };
    }
    return randomIdentity();
}
function getCommentTimeString() {
    const d = new Date();
    const time = d.toLocaleString('default', {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    });
    const date = d.toLocaleString('default', {
        month: 'short',
        day: 'numeric'
    });
    return time + ' ' + date;
}
//function that converts a line-column pairing to an index
function lineToIndex(str, line, col) {
    if (line == 0) {
        return col;
    }
    else {
        let arr = str.split('\n');
        return arr.slice(0, line).join('\n').length + col + 1;
    }
}
function hashString(s) {
    let hash = 0;
    if (s.length == 0) {
        return hash;
    }
    for (let i = 0; i < s.length; i++) {
        let char = s.charCodeAt(i);
        hash = (hash << 5) - hash + char;
        hash = hash & hash; // Convert to 32bit integer
    }
    return hash;
}
function truncate(text, maxLength) {
    return text.length > maxLength ? text.slice(0, maxLength) + '...' : text;
}
function toCodeMirrorPosition(pos) {
    return {
        line: pos.line,
        ch: pos.column
    };
}
function toCodeEditorPosition(pos) {
    return {
        line: pos.line,
        column: pos.ch
    };
}


/***/ }),

/***/ "./lib/api/widget.js":
/*!***************************!*\
  !*** ./lib/api/widget.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommentWidget": () => (/* binding */ CommentWidget),
/* harmony export */   "CommentFileWidget": () => (/* binding */ CommentFileWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./utils */ "./lib/api/utils.js");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./icons */ "./lib/api/icons.js");








function Jdiv(props) {
    return react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", Object.assign({}, props), props.children);
}
function Jspan(props) {
    return react__WEBPACK_IMPORTED_MODULE_1__.createElement("span", Object.assign({}, props), props.children);
}
function ReactMarkdownRenderer(props) {
    const { source, latexTypesetter, linkHandler, resolver, sanitizer, shouldTypeset } = props;
    let node = document.createElement('div');
    const [renderElement, SetRenderElement] = react__WEBPACK_IMPORTED_MODULE_1__.useState(react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", null));
    react__WEBPACK_IMPORTED_MODULE_1__.useEffect(() => {
        const markdownRender = async () => {
            await (0,_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_5__.renderMarkdown)({
                host: node,
                trusted: false,
                source,
                latexTypesetter,
                linkHandler,
                resolver,
                sanitizer,
                shouldTypeset
            });
            SetRenderElement(react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-MarkdownBody", dangerouslySetInnerHTML: {
                    __html: node.innerHTML
                } }));
        };
        void markdownRender();
        return () => SetRenderElement(react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", null));
    }, []);
    return renderElement;
}
/**
 * JMarkdownRender calls the generalizable ReactMarkdownRenderer for our implementation
 */
function JMarkdownRenderer(props) {
    const { registry, isAttached, text } = props;
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(ReactMarkdownRenderer, { source: text, latexTypesetter: registry.latexTypesetter, linkHandler: registry.linkHandler, resolver: registry.resolver, sanitizer: registry.sanitizer, shouldTypeset: isAttached }));
}
/**
 * SubmitButtons returns the set of buttons (submit and cancel) that a comment/reply uses to take in input
 */
function SubmitButtons(props) {
    const { hidden } = props;
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { hidden: hidden, className: "jc-SubmitButtons" },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { hidden: hidden, className: "jc-SubmitButton", jcEventArea: "submit" }, "Submit"),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { hidden: hidden, className: "jc-CancelButton", jcEventArea: "cancel" }, "Cancel")));
}
function JCComment(props) {
    var _a, _b;
    const { comment, editable, preview, renderer, isAttached } = props;
    const className = (_a = props.className) !== null && _a !== void 0 ? _a : '';
    // TODO: Replace `UserIcons[0]` with an error icon (maybe just black circle?)
    const icon = (_b = _icons__WEBPACK_IMPORTED_MODULE_6__.UserIcons[comment.identity.icon]) !== null && _b !== void 0 ? _b : _icons__WEBPACK_IMPORTED_MODULE_6__.UserIcons[0];
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: 'jc-Comment jc-mod-focus-border' + className, id: comment.id, jcEventArea: "other" },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: "jc-CommentProfilePicContainer" },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: "jc-CommentProfilePic", style: { backgroundColor: comment.identity.color }, jcEventArea: "user" },
                react__WEBPACK_IMPORTED_MODULE_1__.createElement(icon.react, { className: "jc-MoonIcon" }))),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement("span", { className: "jc-Nametag" }, comment.identity.name),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jspan, { className: "jc-IconContainer", jcEventArea: "dropdown" },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.ellipsesIcon.react, { className: "jc-Ellipses" })),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement("br", null),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement("span", { className: "jc-Time" }, comment.time),
        preview != null && (react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-Preview" },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-PreviewBar" }),
            react__WEBPACK_IMPORTED_MODULE_1__.createElement("span", { className: "jc-PreviewText" }, preview))),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: "jc-Body", contentEditable: editable, suppressContentEditableWarning: true, jcEventArea: "body", onFocus: (event) => {
                const e = event.target;
                e.innerHTML = `<p>${comment.text}</p>`;
                document.execCommand('selectAll', false, undefined);
            } },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(JMarkdownRenderer, { text: comment.text, registry: renderer, isAttached: isAttached })),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(SubmitButtons, { hidden: !editable })));
}
function JCReply(props) {
    var _a, _b;
    const reply = props.reply;
    const className = (_a = props.className) !== null && _a !== void 0 ? _a : '';
    const editable = props.editable;
    const icon = (_b = _icons__WEBPACK_IMPORTED_MODULE_6__.UserIcons[reply.identity.icon]) !== null && _b !== void 0 ? _b : _icons__WEBPACK_IMPORTED_MODULE_6__.UserIcons[0];
    const renderer = props.renderer;
    const isAttached = props.isAttached;
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: 'jc-Comment jc-Reply jc-mod-focus-border' + className, id: reply.id, jcEventArea: "other" },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: "jc-ReplyPicContainer" },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: "jc-ReplyPic", style: { backgroundColor: reply.identity.color }, jcEventArea: "user" },
                react__WEBPACK_IMPORTED_MODULE_1__.createElement(icon.react, { className: "jc-MoonIcon" }))),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement("span", { className: "jc-Nametag" }, reply.identity.name),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jspan, { className: "jc-IconContainer", jcEventArea: "dropdown" },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.ellipsesIcon.react, { className: "jc-Ellipses" })),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement("br", null),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-ReplySpacer" }),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: "jc-Body", contentEditable: editable, suppressContentEditableWarning: true, jcEventArea: "body", onFocus: (e) => {
                e.target.innerHTML = `<p>${reply.text}</p>`;
                document.execCommand('selectAll', false, undefined);
            } },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement(JMarkdownRenderer, { text: reply.text, registry: renderer, isAttached: isAttached })),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(SubmitButtons, { hidden: !editable })));
}
function JCCommentWithReplies(props) {
    var _a;
    const { comment, editID, collapsed, renderer, isAttached, preview } = props;
    const className = (_a = props.className) !== null && _a !== void 0 ? _a : '';
    let RepliesComponent = () => {
        if (!collapsed || comment.replies.length < 4) {
            return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(react__WEBPACK_IMPORTED_MODULE_1__.Fragment, null,
                react__WEBPACK_IMPORTED_MODULE_1__.createElement(JCComment, { comment: comment, isAttached: isAttached, editable: editID === comment.id, renderer: renderer, preview: preview }),
                react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: 'jc-Replies' }, comment.replies.map(reply => (react__WEBPACK_IMPORTED_MODULE_1__.createElement(JCReply, { reply: reply, isAttached: isAttached, editable: editID === reply.id, renderer: renderer, key: reply.id }))))));
        }
        else {
            return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(react__WEBPACK_IMPORTED_MODULE_1__.Fragment, null,
                react__WEBPACK_IMPORTED_MODULE_1__.createElement(JCComment, { comment: comment, isAttached: isAttached, editable: editID === comment.id, renderer: renderer, preview: preview }),
                react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: 'jc-Replies' },
                    react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: "jc-Replies-breaker jc-mod-focus-border", jcEventArea: "collapser" },
                        react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-Replies-breaker-left" }, "expand thread"),
                        react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-RepliesSpacer" }),
                        react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-Replies-breaker-right" },
                            react__WEBPACK_IMPORTED_MODULE_1__.createElement("hr", null),
                            react__WEBPACK_IMPORTED_MODULE_1__.createElement("hr", null),
                            react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-Replies-breaker-number jc-mod-focus-border" }, comment.replies.length - 1))),
                    react__WEBPACK_IMPORTED_MODULE_1__.createElement(JCReply, { reply: comment.replies[comment.replies.length - 1], editable: editID === comment.replies[comment.replies.length - 1].id, isAttached: isAttached, renderer: renderer, key: comment.replies[comment.replies.length - 1].id }))));
        }
    };
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: 'jc-CommentWithReplies ' + className },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(RepliesComponent, null)));
}
function JCReplyArea(props) {
    const hidden = props.hidden;
    const className = props.className || '';
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { hidden: hidden },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(Jdiv, { className: 'jc-ReplyInputArea jc-mod-focus-border' + className, contentEditable: true, jcEventArea: "reply", onFocus: () => document.execCommand('selectAll', false, undefined), "data-placeholder": "reply" }),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(SubmitButtons, { hidden: hidden })));
}
function JCCommentWrapper(props) {
    const commentWidget = props.commentWidget;
    const className = props.className || '';
    const eventHandler = commentWidget.handleEvent.bind(commentWidget);
    const comment = commentWidget.comment;
    if (comment == null) {
        return react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: "jc-Error" });
    }
    return (react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: className, onClick: eventHandler, onKeyDown: eventHandler },
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(JCCommentWithReplies, { isAttached: commentWidget.isAttached, comment: comment, renderer: commentWidget.renderer, editID: commentWidget.editID, activeID: commentWidget.activeID, collapsed: commentWidget.collapsed, preview: commentWidget.getPreview() }),
        react__WEBPACK_IMPORTED_MODULE_1__.createElement(JCReplyArea, { hidden: commentWidget.replyAreaHidden })));
}
/**
 * A React widget that can render a comment and its replies.
 */
class CommentWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    constructor(options) {
        super();
        this._replyAreaHidden = true;
        this._editID = '';
        this._renderNeeded = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal(this);
        this._collapsed = true;
        const { target, model, comment, isMock } = options;
        this.id = comment.id;
        this._commentID = comment.id;
        this._activeID = comment.id;
        this._target = target;
        this._model = model;
        this._comment = comment;
        this._isMock = isMock !== null && isMock !== void 0 ? isMock : false;
        this.addClass('jc-CommentWidget');
        this.node.tabIndex = 0;
    }
    onAfterAttach(msg) {
        super.onAfterAttach(msg);
        if (this.isMock) {
            this.openEditActive();
        }
    }
    toJSON() {
        return this.comment;
    }
    getPreview() {
        return;
    }
    handleEvent(event) {
        switch (event.type) {
            case 'click':
                this._handleClick(event);
                break;
            case 'keydown':
                this._handleKeydown(event);
                break;
        }
    }
    /**
     * Handle `click` events on the widget.
     */
    _handleClick(event) {
        switch (CommentWidget.getEventArea(event)) {
            case 'body':
                this._handleBodyClick(event);
                break;
            case 'dropdown':
                this._handleDropdownClick(event);
                break;
            case 'reply':
                this._handleReplyClick(event);
                break;
            case 'user':
                this._handleUserClick(event);
                break;
            case 'other':
                this._handleOtherClick(event);
                break;
            case 'collapser':
                this._handleCollapserClick(event);
                break;
            case 'submit':
                this._handleSubmitClick(event);
                break;
            case 'cancel':
                this._handleCancelClick(event);
                break;
            case 'none':
                break;
            default:
                break;
        }
    }
    _handleCollapserClick(event) {
        this._setClickFocus(event);
        this.collapsed = false;
        this.revealReply();
    }
    /**
     * Collapses and hides the reply area of other comment widgets in the same panel.
     */
    _collapseOtherComments() {
        const parent = this.parent;
        if (parent == null) {
            return;
        }
        const commentFileWidget = parent;
        if (commentFileWidget.expandedCommentID === this.id) {
            return;
        }
        const widgets = commentFileWidget.widgets;
        widgets.forEach(widget => {
            if (widget.id !== this.id) {
                widget.collapsed = true;
                widget.replyAreaHidden = true;
                widget.editID = '';
            }
        });
        commentFileWidget.expandedCommentID = this.id;
    }
    /**
     * Scrolls to the comment's target, if it exists
     */
    _scrollToTarget() {
        const element = this.element;
        if (element != null) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    }
    /**
     * Sets the widget focus and active id on click.
     *
     * A building block of other click handlers.
     */
    _setClickFocus(event) {
        const oldActive = document.activeElement;
        const target = event.target;
        const clickID = Private.getClickID(target);
        if (clickID != null) {
            this.activeID = clickID;
        }
        if (oldActive == null || !this.node.contains(oldActive)) {
            this.node.focus();
        }
        this._collapseOtherComments();
    }
    /**
     * Handle a click on the submit button when commenting.
     */
    _handleSubmitClick(event) {
        this._setClickFocus(event);
        const target = event.target;
        event.preventDefault();
        event.stopPropagation();
        const element = target.parentNode.previousSibling;
        if (element == null) {
            return;
        }
        if (element.classList.contains('jc-ReplyInputArea')) {
            //  reply
            if (!/\S/.test(element.innerText)) {
                return;
            }
            this.model.addReply({
                identity: (0,_utils__WEBPACK_IMPORTED_MODULE_7__.getIdentity)(this.model.awareness),
                text: element.innerText
            }, this.commentID);
            this.editID = '';
            element.textContent = '';
            this.replyAreaHidden = true;
            return;
        }
        if (!/\S/.test(element.innerText)) {
            if (this.isMock) {
                this.dispose();
                return;
            }
            element.innerText = this.text;
        }
        else {
            if (this.isMock) {
                this.populate(element.innerText);
                return;
            }
            this.editActive(element.innerText);
        }
        this.editID = '';
    }
    /**
     * Handle a click on the cancel button when commenting.
     */
    _handleCancelClick(event) {
        this._setClickFocus(event);
        const target = event.target;
        event.preventDefault();
        event.stopPropagation();
        if (this.isMock) {
            this.dispose();
        }
        const element = target.parentNode.previousSibling;
        if (element == null) {
            return;
        }
        if (element.classList.contains('jc-ReplyInputArea')) {
            this.replyAreaHidden = true;
        }
        this.editID = '';
        element.blur();
    }
    /**
     * Handle a click on the dropdown (ellipses) area of a widget.
     */
    _handleDropdownClick(event) {
        this._setClickFocus(event);
        const menu = this.menu;
        if (menu != null && !this.isMock) {
            menu.open(event.pageX, event.pageY);
        }
    }
    /**
     * Handle a click on the user icon area of a widget.
     *
     * ### Note
     * Currently just acts as an `other` click.
     */
    _handleUserClick(event) {
        console.log('clicked user photo!');
        this._setClickFocus(event);
        this._scrollToTarget();
    }
    /**
     * Handle a click on the widget but not on a specific area.
     */
    _handleOtherClick(event) {
        this._setClickFocus(event);
        const target = event.target;
        const clickID = Private.getClickID(target);
        if (clickID == null) {
            return;
        }
        this.editID = '';
        if (this.replyAreaHidden) {
            this.revealReply();
        }
        else {
            this.replyAreaHidden = true;
        }
        this._scrollToTarget();
    }
    /**
     * Handle a click on the widget's reply area.
     */
    _handleReplyClick(event) {
        this._setClickFocus(event);
        this._scrollToTarget();
    }
    /**
     * Handle a click on the widget's body.
     */
    _handleBodyClick(event) {
        this._setClickFocus(event);
        this._scrollToTarget();
    }
    /**
     * Handle `keydown` events on the widget.
     */
    _handleKeydown(event) {
        switch (CommentWidget.getEventArea(event)) {
            case 'reply':
                this._handleReplyKeydown(event);
                break;
            case 'body':
                this._handleBodyKeydown(event);
                break;
            default:
                break;
        }
    }
    /**
     * Handle a keydown on the widget's reply area.
     */
    _handleReplyKeydown(event) {
        if (event.key === 'Escape') {
            this.replyAreaHidden = true;
            return;
        }
        else if (event.key === 'Tab') {
            event.preventDefault();
            document.execCommand('insertHTML', false, '&#009');
            return;
        }
        else if (event.key !== 'Enter') {
            return;
        }
        else if (event.shiftKey) {
            const target = event.target;
            event.preventDefault();
            event.stopPropagation();
            if (!/\S/.test(target.innerText)) {
                return;
            }
            this.model.addReply({
                identity: (0,_utils__WEBPACK_IMPORTED_MODULE_7__.getIdentity)(this.model.awareness),
                text: target.innerText
            }, this.commentID);
            this.editID = '';
            target.textContent = '';
            this.replyAreaHidden = true;
        }
    }
    /**
     * Handle a keydown on the widget's body.
     */
    _handleBodyKeydown(event) {
        if (this.editID === '') {
            return;
        }
        const target = event.target;
        switch (event.key) {
            case 'Tab':
                event.preventDefault();
                document.execCommand('insertHTML', false, '&#009');
                break;
            case 'Escape':
                event.preventDefault();
                event.stopPropagation();
                if (this.isMock) {
                    this.dispose();
                    break;
                }
                target.innerText = this.text;
                this.editID = '';
                target.blur();
                break;
            case 'Enter':
                if (!event.shiftKey) {
                    break;
                }
                event.preventDefault();
                event.stopPropagation();
                if (this.isMock) {
                    if (/\S/.test(target.innerText)) {
                        this.populate(target.innerText);
                    }
                    else {
                        this.dispose();
                    }
                    break;
                }
                if (!/\S/.test(target.innerText)) {
                    target.innerText = this.text;
                }
                else {
                    this.editActive(target.innerText);
                }
                this.editID = '';
                target.blur();
                break;
            default:
                break;
        }
    }
    populate(text) {
        if (!this.isMock) {
            return;
        }
        let index = 0;
        let node = this.node;
        while (node.previousSibling != null) {
            index++;
            node = node.previousSibling;
        }
        this.hide();
        const { identity, type } = this.comment;
        const source = this.target;
        this.model.insertComment({
            text,
            identity,
            type,
            source
        }, index);
        this.dispose();
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.UseSignal, { signal: this.renderNeeded }, () => react__WEBPACK_IMPORTED_MODULE_1__.createElement(JCCommentWrapper, { commentWidget: this })));
    }
    /**
     * Open the widget's reply area and focus on it.
     */
    revealReply() {
        if (this.isAttached === false) {
            return;
        }
        this.replyAreaHidden = false;
        const nodes = this.node.getElementsByClassName('jc-ReplyInputArea');
        nodes[0].focus();
    }
    /**
     * Select the body area of the currently active comment for editing.
     */
    openEditActive() {
        if (this.isAttached === false) {
            return;
        }
        this.editID = this.activeID;
        const comment = document.getElementById(this.activeID);
        if (comment == null) {
            return;
        }
        const elements = comment.getElementsByClassName('jc-Body');
        const target = elements[0];
        target.focus();
    }
    editActive(text) {
        if (this.activeID === this.commentID) {
            this.model.editComment({ text }, this.commentID);
        }
        else {
            this.model.editReply({ text }, this.activeID, this.commentID);
        }
    }
    /**
     * Delete the currently active comment or reply.
     *
     * ### Notes
     * If the base comment is deleted, the widget will be disposed.
     */
    deleteActive() {
        if (this.isAttached === false) {
            return;
        }
        if (this.activeID === this.commentID) {
            this.model.deleteComment(this.commentID);
            this.dispose();
        }
        else {
            this.model.deleteReply(this.activeID, this.commentID);
        }
    }
    /**
     * The comment object being rendered by the widget.
     */
    get comment() {
        if (this.isMock) {
            return this._comment;
        }
        const loc = this.model.getComment(this.commentID);
        return loc ? loc.comment : this._comment;
    }
    /**
     * The target of the comment (what is being commented on).
     */
    get target() {
        return this._target;
    }
    /**
     * Information about the author of the comment.
     */
    get identity() {
        return this.comment.identity;
    }
    /**
     * The type of the comment.
     */
    get type() {
        return this.comment.type;
    }
    /**
     * The plain body text of the comment.
     */
    get text() {
        return this.comment.text;
    }
    /**
     * An array of replies to the comment.
     */
    get replies() {
        return this.comment.replies;
    }
    /**
     * The ID of the main comment.
     */
    get commentID() {
        return this._commentID;
    }
    get model() {
        return this._model;
    }
    /**
     * The ID of the last-focused comment or reply.
     */
    get activeID() {
        return this._activeID;
    }
    set activeID(newVal) {
        if (newVal !== this.activeID) {
            this._activeID = newVal;
            this._renderNeeded.emit(undefined);
        }
    }
    /**
     * Whether to show the reply area or not
     */
    get replyAreaHidden() {
        return this._replyAreaHidden;
    }
    set replyAreaHidden(newVal) {
        if (newVal !== this.replyAreaHidden) {
            this._replyAreaHidden = newVal;
            this._renderNeeded.emit(undefined);
        }
    }
    /**
     * A signal emitted when a React re-render is required.
     */
    get renderNeeded() {
        return this._renderNeeded;
    }
    get collapsed() {
        return this._collapsed;
    }
    set collapsed(newVal) {
        if (newVal !== this.collapsed) {
            this._collapsed = newVal;
            this._renderNeeded.emit(undefined);
        }
    }
    /**
     * The ID of the managed comment being edited, or the empty string if none.
     */
    get editID() {
        return this._editID;
    }
    set editID(newVal) {
        if (this.editID !== newVal) {
            this._editID = newVal;
            this._renderNeeded.emit(undefined);
        }
    }
    get menu() {
        return this.model.commentMenu;
    }
    get renderer() {
        return this.parent.renderer;
    }
    get isMock() {
        return this._isMock;
    }
    set isMock(newVal) {
        this._isMock = newVal;
    }
    get element() {
        return;
    }
}
(function (CommentWidget) {
    /**
     * Whether a string is a type of `EventArea`
     */
    function isEventArea(input) {
        return [
            'dropdown',
            'body',
            'user',
            'reply',
            'other',
            'collapser',
            'submit',
            'cancel'
        ].includes(input);
    }
    CommentWidget.isEventArea = isEventArea;
    /**
     * Gets the `EventArea` of an event on a `CommentWidget`.
     *
     * Returns `none` if the event has no ancestors with the `jcEventArea` attribute,
     * and returns `other` if `jcEventArea` is set but the value is unrecognized.
     *
     * ### Notes
     * Also sets the target of the event to the first ancestor of the target with
     * the `jcEventArea` attribute set.
     */
    function getEventArea(event) {
        const target = event.target;
        const areaElement = target.closest('[jcEventArea]');
        if (areaElement == null) {
            return 'none';
        }
        const area = areaElement.getAttribute('jcEventArea');
        if (area == null) {
            return 'other';
        }
        event.target = areaElement;
        return isEventArea(area) ? area : 'other';
    }
    CommentWidget.getEventArea = getEventArea;
})(CommentWidget || (CommentWidget = {}));
/**
 * A widget that hosts and displays a list of `CommentWidget`s
 */
class CommentFileWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Panel {
    constructor(options, renderer) {
        super();
        this._commentAdded = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal(this);
        const { context } = options;
        this._context = context;
        this._model = context.model;
        this._model.widgets = this.widgets;
        this.id = `Comments-${context.path}`;
        this.addClass('jc-CommentFileWidget');
        this.renderer = renderer;
    }
    insertComment(comment, index) {
        const factory = this.model.commentWidgetRegistry.getFactory(comment.type);
        if (factory == null) {
            return;
        }
        const widget = factory.createWidget(comment, this.model);
        if (widget != null) {
            this.insertWidget(index, widget);
            this._commentAdded.emit(widget);
        }
    }
    initialize() {
        while (this.widgets.length > 0) {
            this.widgets[0].dispose();
        }
        this.model.comments.forEach(comment => this.addComment(comment));
    }
    addComment(comment) {
        this.insertComment(comment, this.widgets.length);
    }
    get model() {
        return this._model;
    }
    get context() {
        return this._context;
    }
    get registry() {
        return this.renderer;
    }
    get commentAdded() {
        return this._commentAdded;
    }
    get expandedCommentID() {
        return this._expandedCommentID;
    }
    set expandedCommentID(newVal) {
        this._expandedCommentID = newVal;
    }
}
var Private;
(function (Private) {
    /**
     * Get the ID of a comment that a target lies within.
     */
    function getClickID(target) {
        const comment = target.closest('.jc-Comment');
        if (comment == null) {
            return undefined;
        }
        return comment.id;
    }
    Private.getClickID = getClickID;
})(Private || (Private = {}));


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "BlueCreateCommentIcon": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.BlueCreateCommentIcon),
/* harmony export */   "CommentFactory": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentFactory),
/* harmony export */   "CommentFileModel": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentFileModel),
/* harmony export */   "CommentFileModelFactory": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentFileModelFactory),
/* harmony export */   "CommentFileWidget": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentFileWidget),
/* harmony export */   "CommentPanel": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentPanel),
/* harmony export */   "CommentRegistry": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentRegistry),
/* harmony export */   "CommentWidget": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidget),
/* harmony export */   "CommentWidgetFactory": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidgetFactory),
/* harmony export */   "CommentWidgetRegistry": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidgetRegistry),
/* harmony export */   "CommentsHubIcon": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentsHubIcon),
/* harmony export */   "CommentsPanelIcon": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CommentsPanelIcon),
/* harmony export */   "CreateCommentIcon": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.CreateCommentIcon),
/* harmony export */   "ICommentPanel": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.ICommentPanel),
/* harmony export */   "ICommentRegistry": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.ICommentRegistry),
/* harmony export */   "ICommentWidgetRegistry": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.ICommentWidgetRegistry),
/* harmony export */   "NewCommentButton": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.NewCommentButton),
/* harmony export */   "OrangeCreateCommentIcon": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.OrangeCreateCommentIcon),
/* harmony export */   "PanelHeader": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.PanelHeader),
/* harmony export */   "UserIcons": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.UserIcons),
/* harmony export */   "commentRegistryPlugin": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.commentRegistryPlugin),
/* harmony export */   "commentWidgetRegistryPlugin": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.commentWidgetRegistryPlugin),
/* harmony export */   "emptyIdentity": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.emptyIdentity),
/* harmony export */   "getCommentTimeString": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.getCommentTimeString),
/* harmony export */   "getIdentity": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.getIdentity),
/* harmony export */   "hashString": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.hashString),
/* harmony export */   "jupyterCommentingPlugin": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.jupyterCommentingPlugin),
/* harmony export */   "lineToIndex": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.lineToIndex),
/* harmony export */   "randomColor": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.randomColor),
/* harmony export */   "randomIcon": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.randomIcon),
/* harmony export */   "randomIdentity": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.randomIdentity),
/* harmony export */   "setIdentityName": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.setIdentityName),
/* harmony export */   "toCodeEditorPosition": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.toCodeEditorPosition),
/* harmony export */   "toCodeMirrorPosition": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.toCodeMirrorPosition),
/* harmony export */   "truncate": () => (/* reexport safe */ _api__WEBPACK_IMPORTED_MODULE_0__.truncate),
/* harmony export */   "CellCommentFactory": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.CellCommentFactory),
/* harmony export */   "CellCommentWidget": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.CellCommentWidget),
/* harmony export */   "CellCommentWidgetFactory": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.CellCommentWidgetFactory),
/* harmony export */   "CellSelectionCommentFactory": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.CellSelectionCommentFactory),
/* harmony export */   "CellSelectionCommentWidget": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.CellSelectionCommentWidget),
/* harmony export */   "CellSelectionCommentWidgetFactory": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.CellSelectionCommentWidgetFactory),
/* harmony export */   "CommandIDs": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.CommandIDs),
/* harmony export */   "docFromCell": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.docFromCell),
/* harmony export */   "markCommentSelection": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.markCommentSelection),
/* harmony export */   "notebookCommentsPlugin": () => (/* reexport safe */ _notebook__WEBPACK_IMPORTED_MODULE_1__.notebookCommentsPlugin),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./api */ "./lib/api/plugin.js");
/* harmony import */ var _text_plugin__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./text/plugin */ "./lib/text/plugin.js");
/* harmony import */ var _notebook__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./notebook */ "./lib/notebook/plugin.js");
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./api */ "./lib/api/index.js");
/* harmony import */ var _notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./notebook */ "./lib/notebook/index.js");
/* harmony import */ var _text__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./text */ "./lib/text.js");
/* harmony import */ var _text__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_text__WEBPACK_IMPORTED_MODULE_2__);
/* harmony reexport (unknown) */ var __WEBPACK_REEXPORT_OBJECT__ = {};
/* harmony reexport (unknown) */ for(const __WEBPACK_IMPORT_KEY__ in _text__WEBPACK_IMPORTED_MODULE_2__) if(["default","BlueCreateCommentIcon","CommentFactory","CommentFileModel","CommentFileModelFactory","CommentFileWidget","CommentPanel","CommentRegistry","CommentWidget","CommentWidgetFactory","CommentWidgetRegistry","CommentsHubIcon","CommentsPanelIcon","CreateCommentIcon","ICommentPanel","ICommentRegistry","ICommentWidgetRegistry","NewCommentButton","OrangeCreateCommentIcon","PanelHeader","UserIcons","commentRegistryPlugin","commentWidgetRegistryPlugin","emptyIdentity","getCommentTimeString","getIdentity","hashString","jupyterCommentingPlugin","lineToIndex","randomColor","randomIcon","randomIdentity","setIdentityName","toCodeEditorPosition","toCodeMirrorPosition","truncate","CellCommentFactory","CellCommentWidget","CellCommentWidgetFactory","CellSelectionCommentFactory","CellSelectionCommentWidget","CellSelectionCommentWidgetFactory","CommandIDs","docFromCell","markCommentSelection","notebookCommentsPlugin"].indexOf(__WEBPACK_IMPORT_KEY__) < 0) __WEBPACK_REEXPORT_OBJECT__[__WEBPACK_IMPORT_KEY__] = () => _text__WEBPACK_IMPORTED_MODULE_2__[__WEBPACK_IMPORT_KEY__]
/* harmony reexport (unknown) */ __webpack_require__.d(__webpack_exports__, __WEBPACK_REEXPORT_OBJECT__);

// Importing directly from './text' causes the imported plugin to be undefined (??)





const plugins = [
    _api__WEBPACK_IMPORTED_MODULE_3__.jupyterCommentingPlugin,
    _api__WEBPACK_IMPORTED_MODULE_3__.commentRegistryPlugin,
    _api__WEBPACK_IMPORTED_MODULE_3__.commentWidgetRegistryPlugin,
    _notebook__WEBPACK_IMPORTED_MODULE_4__.notebookCommentsPlugin,
    _text_plugin__WEBPACK_IMPORTED_MODULE_5__.textCommentingPlugin
];
/**
 * Export the plugins as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "./lib/notebook/commentfactory.js":
/*!****************************************!*\
  !*** ./lib/notebook/commentfactory.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CellCommentFactory": () => (/* binding */ CellCommentFactory),
/* harmony export */   "CellSelectionCommentFactory": () => (/* binding */ CellSelectionCommentFactory)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/factory.js");

class CellCommentFactory extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentFactory {
    constructor() {
        super(...arguments);
        this.type = 'cell';
    }
    createComment(options) {
        const comment = super.createComment(options);
        comment.target = { cellID: options.source.model.id };
        return comment;
    }
}
class CellSelectionCommentFactory extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentFactory {
    constructor() {
        super(...arguments);
        this.type = 'cell-selection';
    }
    createComment(options) {
        const comment = super.createComment(options);
        const { start, end } = options.source.editor.getSelection();
        comment.target = {
            cellID: options.source.model.id,
            start,
            end
        };
        return comment;
    }
}


/***/ }),

/***/ "./lib/notebook/index.js":
/*!*******************************!*\
  !*** ./lib/notebook/index.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CellCommentFactory": () => (/* reexport safe */ _commentfactory__WEBPACK_IMPORTED_MODULE_0__.CellCommentFactory),
/* harmony export */   "CellSelectionCommentFactory": () => (/* reexport safe */ _commentfactory__WEBPACK_IMPORTED_MODULE_0__.CellSelectionCommentFactory),
/* harmony export */   "CommandIDs": () => (/* reexport safe */ _plugin__WEBPACK_IMPORTED_MODULE_1__.CommandIDs),
/* harmony export */   "notebookCommentsPlugin": () => (/* reexport safe */ _plugin__WEBPACK_IMPORTED_MODULE_1__.notebookCommentsPlugin),
/* harmony export */   "docFromCell": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_2__.docFromCell),
/* harmony export */   "markCommentSelection": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_2__.markCommentSelection),
/* harmony export */   "CellCommentWidget": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.CellCommentWidget),
/* harmony export */   "CellSelectionCommentWidget": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.CellSelectionCommentWidget),
/* harmony export */   "CellCommentWidgetFactory": () => (/* reexport safe */ _widgetfactory__WEBPACK_IMPORTED_MODULE_4__.CellCommentWidgetFactory),
/* harmony export */   "CellSelectionCommentWidgetFactory": () => (/* reexport safe */ _widgetfactory__WEBPACK_IMPORTED_MODULE_4__.CellSelectionCommentWidgetFactory)
/* harmony export */ });
/* harmony import */ var _commentfactory__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./commentfactory */ "./lib/notebook/commentfactory.js");
/* harmony import */ var _plugin__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./plugin */ "./lib/notebook/plugin.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils */ "./lib/notebook/utils.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./widget */ "./lib/notebook/widget.js");
/* harmony import */ var _widgetfactory__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widgetfactory */ "./lib/notebook/widgetfactory.js");








/***/ }),

/***/ "./lib/notebook/plugin.js":
/*!********************************!*\
  !*** ./lib/notebook/plugin.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommandIDs": () => (/* binding */ CommandIDs),
/* harmony export */   "notebookCommentsPlugin": () => (/* binding */ notebookCommentsPlugin),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../api */ "./lib/api/token.js");
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../api */ "./lib/api/utils.js");
/* harmony import */ var _commentfactory__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./commentfactory */ "./lib/notebook/commentfactory.js");
/* harmony import */ var _widgetfactory__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./widgetfactory */ "./lib/notebook/widgetfactory.js");




var CommandIDs;
(function (CommandIDs) {
    CommandIDs.addNotebookComment = 'jl-comments:add-notebook-comment';
})(CommandIDs || (CommandIDs = {}));
/**
 * A plugin that allows notebooks to be commented on.
 */
const notebookCommentsPlugin = {
    id: 'jupyterlab-comments:notebook',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker, _api__WEBPACK_IMPORTED_MODULE_1__.ICommentPanel],
    activate: (app, nbTracker, panel) => {
        const commentRegistry = panel.commentRegistry;
        const commentWidgetRegistry = panel.commentWidgetRegistry;
        commentRegistry.addFactory(new _commentfactory__WEBPACK_IMPORTED_MODULE_2__.CellCommentFactory());
        commentRegistry.addFactory(new _commentfactory__WEBPACK_IMPORTED_MODULE_2__.CellSelectionCommentFactory());
        commentWidgetRegistry.addFactory(new _widgetfactory__WEBPACK_IMPORTED_MODULE_3__.CellCommentWidgetFactory({ commentRegistry, tracker: nbTracker }));
        commentWidgetRegistry.addFactory(new _widgetfactory__WEBPACK_IMPORTED_MODULE_3__.CellSelectionCommentWidgetFactory({
            commentRegistry,
            tracker: nbTracker
        }));
        app.commands.addCommand(CommandIDs.addNotebookComment, {
            label: 'Add Comment',
            execute: () => {
                const cell = nbTracker.activeCell;
                if (cell == null) {
                    return;
                }
                const model = panel.model;
                if (model == null) {
                    return;
                }
                const comments = model.comments;
                let index = comments.length;
                for (let i = comments.length; i > 0; i--) {
                    const comment = comments.get(i - 1);
                    if (comment.target.cellID === cell.model.id) {
                        index = i;
                    }
                }
                const { start, end } = cell.editor.getSelection();
                const type = start.column === end.column && start.line === end.line
                    ? 'cell'
                    : 'cell-selection';
                panel.mockComment({
                    identity: (0,_api__WEBPACK_IMPORTED_MODULE_4__.getIdentity)(model.awareness),
                    type,
                    source: cell
                }, index);
            }
        });
        // This updates the indicator and scrolls to the comments of the selected cell
        // when the active cell changes.
        let currentCell = null;
        nbTracker.activeCellChanged.connect((_, cell) => {
            // Clean up old mouseup listener
            document.removeEventListener('mouseup', onMouseup);
            currentCell = cell;
            panel.button.close();
            // panel.model can be null when the notebook is first loaded
            if (cell == null || panel.model == null) {
                return;
            }
            // Scroll to the first comment associated with the currently selected cell.
            for (let comment of panel.model.comments) {
                if (comment.type === 'cell-selection' || comment.type === 'cell') {
                    const cellComment = comment;
                    if (cellComment.target.cellID === cell.model.id) {
                        panel.scrollToComment(cellComment.id);
                        break;
                    }
                }
            }
        });
        let currentSelection;
        // Opens add comment button on the current cell when the mouse is released
        // after a text selection
        const onMouseup = (_) => {
            if (currentCell == null || currentCell.isDisposed) {
                return;
            }
            const editor = currentCell.editor;
            const { top } = editor.getCoordinateForPosition(currentSelection.start);
            const { bottom } = editor.getCoordinateForPosition(currentSelection.end);
            const { right } = currentCell.editorWidget.node.getBoundingClientRect();
            const node = nbTracker.currentWidget.content.node;
            panel.button.open(right - 10, (top + bottom) / 2 - 10, () => app.commands.execute(CommandIDs.addNotebookComment), node);
        };
        // Adds a single-run mouseup listener whenever a text selection is made in a cell
        const awarenessHandler = () => {
            if (currentCell == null) {
                return;
            }
            currentSelection = currentCell.editor.getSelection();
            const { start, end } = currentSelection;
            if (start.column !== end.column || start.line !== end.line) {
                document.addEventListener('mouseup', onMouseup, { once: true });
            }
            else {
                panel.button.close();
            }
        };
        let lastAwareness = null;
        nbTracker.currentChanged.connect((_, notebook) => {
            if (notebook == null) {
                lastAwareness = null;
                return;
            }
            // Clean up old awareness handler
            if (lastAwareness != null) {
                lastAwareness.off('change', awarenessHandler);
            }
            // Add new awareness handler
            const model = notebook.model.sharedModel;
            model.awareness.on('change', awarenessHandler);
            lastAwareness = model.awareness;
        });
        app.contextMenu.addItem({
            command: CommandIDs.addNotebookComment,
            selector: '.jp-Notebook .jp-Cell',
            rank: 13
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (notebookCommentsPlugin);


/***/ }),

/***/ "./lib/notebook/utils.js":
/*!*******************************!*\
  !*** ./lib/notebook/utils.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "docFromCell": () => (/* binding */ docFromCell),
/* harmony export */   "markCommentSelection": () => (/* binding */ markCommentSelection)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/utils.js");

function docFromCell(cell) {
    return cell.editorWidget.editor.doc;
}
function markCommentSelection(doc, comment) {
    const color = comment.identity.color;
    const r = parseInt(color.slice(1, 3), 16);
    const g = parseInt(color.slice(3, 5), 16);
    const b = parseInt(color.slice(5, 7), 16);
    const { start, end } = comment.target;
    const forward = start.line < end.line ||
        (start.line === end.line && start.column <= end.column);
    const anchor = (0,_api__WEBPACK_IMPORTED_MODULE_0__.toCodeMirrorPosition)(forward ? start : end);
    const head = (0,_api__WEBPACK_IMPORTED_MODULE_0__.toCodeMirrorPosition)(forward ? end : start);
    return doc.markText(anchor, head, {
        className: 'jc-Highlight',
        title: `${comment.identity.name}: ${(0,_api__WEBPACK_IMPORTED_MODULE_0__.truncate)(comment.text, 140)}`,
        css: `background-color: rgba( ${r}, ${g}, ${b}, 0.15)`,
        attributes: { id: `CommentMark-${comment.id}` }
    });
}


/***/ }),

/***/ "./lib/notebook/widget.js":
/*!********************************!*\
  !*** ./lib/notebook/widget.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CellCommentWidget": () => (/* binding */ CellCommentWidget),
/* harmony export */   "CellSelectionCommentWidget": () => (/* binding */ CellSelectionCommentWidget)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/widget.js");
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../api */ "./lib/api/utils.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils */ "./lib/notebook/utils.js");


class CellCommentWidget extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidget {
    constructor(options) {
        super(options);
    }
    get element() {
        return this.target.node;
    }
}
class CellSelectionCommentWidget extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidget {
    constructor(options) {
        super(options);
        this._mark = options.mark;
    }
    dispose() {
        this._mark.clear();
        super.dispose();
    }
    get element() {
        return this.target.node;
    }
    toJSON() {
        const json = super.toJSON();
        const mark = this._mark;
        if (mark == null) {
            console.warn('No mark found--serializing based on initial text selection position', this);
            return json;
        }
        const range = mark.find();
        if (range == null) {
            console.warn('Mark no longer exists in code editor--serializing based on initial text selection position', this);
            return json;
        }
        const { from, to } = range;
        const textSelectionComment = json;
        textSelectionComment.target.cellID = this.target.model.id;
        textSelectionComment.target.start = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeEditorPosition)(from);
        textSelectionComment.target.end = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeEditorPosition)(to);
        return textSelectionComment;
    }
    getPreview() {
        if (this.isMock || this._mark == null) {
            return Private.getMockCommentPreviewText(this._doc, this.comment);
        }
        const range = this._mark.find();
        if (range == null) {
            return '';
        }
        const { from, to } = range;
        const text = this._doc.getRange(from, to);
        return (0,_api__WEBPACK_IMPORTED_MODULE_1__.truncate)(text, 140);
    }
    get _doc() {
        return (0,_utils__WEBPACK_IMPORTED_MODULE_2__.docFromCell)(this.target);
    }
}
var Private;
(function (Private) {
    function getMockCommentPreviewText(doc, comment) {
        const { start, end } = comment.target;
        const forward = start.line < end.line ||
            (start.line === end.line && start.column <= end.column);
        const from = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeMirrorPosition)(forward ? start : end);
        const to = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeMirrorPosition)(forward ? end : start);
        const text = doc.getRange(from, to);
        return (0,_api__WEBPACK_IMPORTED_MODULE_1__.truncate)(text, 140);
    }
    Private.getMockCommentPreviewText = getMockCommentPreviewText;
})(Private || (Private = {}));


/***/ }),

/***/ "./lib/notebook/widgetfactory.js":
/*!***************************************!*\
  !*** ./lib/notebook/widgetfactory.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CellCommentWidgetFactory": () => (/* binding */ CellCommentWidgetFactory),
/* harmony export */   "CellSelectionCommentWidgetFactory": () => (/* binding */ CellSelectionCommentWidgetFactory)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/factory.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./widget */ "./lib/notebook/widget.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils */ "./lib/notebook/utils.js");



class CellCommentWidgetFactory extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidgetFactory {
    constructor(options) {
        super(options);
        this.widgetType = 'cell';
        this.commentType = 'cell';
        this._tracker = options.tracker;
    }
    createWidget(comment, model, target) {
        const cell = target !== null && target !== void 0 ? target : this._cellFromID(comment.target.cellID);
        if (cell == null) {
            console.error('Cell not found for comment', comment);
            return;
        }
        return new _widget__WEBPACK_IMPORTED_MODULE_1__.CellCommentWidget({
            model,
            comment,
            target: cell
        });
    }
    _cellFromID(id) {
        const notebook = this._tracker.currentWidget;
        if (notebook == null) {
            return;
        }
        return notebook.content.widgets.find(cell => cell.model.id === id);
    }
}
class CellSelectionCommentWidgetFactory extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidgetFactory {
    constructor(options) {
        super(options);
        this.widgetType = 'cell-selection';
        this.commentType = 'cell-selection';
        this._tracker = options.tracker;
    }
    createWidget(comment, model, target) {
        const cell = target !== null && target !== void 0 ? target : this._cellFromID(comment.target.cellID);
        if (cell == null) {
            console.error('Cell not found for comment', comment);
            return;
        }
        const mark = (0,_utils__WEBPACK_IMPORTED_MODULE_2__.markCommentSelection)((0,_utils__WEBPACK_IMPORTED_MODULE_2__.docFromCell)(cell), comment);
        return new _widget__WEBPACK_IMPORTED_MODULE_1__.CellSelectionCommentWidget({
            model,
            comment,
            mark,
            target: cell
        });
    }
    _cellFromID(id) {
        const notebook = this._tracker.currentWidget;
        if (notebook == null) {
            return;
        }
        return notebook.content.widgets.find(cell => cell.model.id === id);
    }
}


/***/ }),

/***/ "./lib/text.js":
/*!*********************!*\
  !*** ./lib/text.js ***!
  \*********************/
/***/ (() => {


// import * as Y from 'yjs';
// import { Widget } from '@lumino/widgets';
// import { ISharedText } from '@jupyterlab/shared-models';
// import { Message } from "@lumino/messaging";
// export class CommentWidget extends Widget implements ISharedText {
//   constructor(ytext: Y.Text) {
//     const node = document.createElement('input');
//     node.type = 'text';
//     node.value = ytext.toString();
//     super({ node });
//     this._ytext = ytext
//     this._undoManager = new Y.UndoManager(this._ytext);
//     this._ytext.observe(this._modelObserver);
//   }
//   handleEvent(event: Event) {
//     switch (event.type) {
//       case 'change':
//         this._handleChange(event as KeyboardEvent);
//         break;
//       default:
//         break;
//     }
//   }
//   private _handleChange(event: KeyboardEvent): void {
//     event.key
//   }
//   protected onAfterAttach(msg: Message): void {
//     super.onAfterAttach(msg);
//     this.node.addEventListener('change', this);
//   }
//   protected onBeforeDetach(msg: Message): void {
//     super.onBeforeDetach(msg);
//     this.node.removeEventListener('change', this);
//   }
//   private _modelObserver(event: Y.YTextEvent): void {
//   }
//   private _ytext: Y.Text;
//   private _undoManager: Y.UndoManager;
// }


/***/ }),

/***/ "./lib/text/commentfactory.js":
/*!************************************!*\
  !*** ./lib/text/commentfactory.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TextSelectionCommentFactory": () => (/* binding */ TextSelectionCommentFactory)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/factory.js");

class TextSelectionCommentFactory extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentFactory {
    constructor() {
        super(...arguments);
        this.type = 'text-selection';
    }
    createComment(options) {
        const comment = super.createComment(options);
        const wrapper = options.source;
        let { start, end } = wrapper.editor.getSelection();
        if (start.line > end.line ||
            (start.line === end.line && start.column > end.column)) {
            [start, end] = [end, start];
        }
        comment.target = { start, end };
        return comment;
    }
}


/***/ }),

/***/ "./lib/text/plugin.js":
/*!****************************!*\
  !*** ./lib/text/plugin.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "textCommentingPlugin": () => (/* binding */ textCommentingPlugin),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../api */ "./lib/api/token.js");
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../api */ "./lib/api/utils.js");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _commentfactory__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./commentfactory */ "./lib/text/commentfactory.js");
/* harmony import */ var _widgetfactory__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widgetfactory */ "./lib/text/widgetfactory.js");





var CommandIDs;
(function (CommandIDs) {
    CommandIDs.addComment = 'jupyter-comments:add-text-comment';
})(CommandIDs || (CommandIDs = {}));
const textCommentingPlugin = {
    id: 'jupyterlab-comments:text',
    autoStart: true,
    requires: [_api__WEBPACK_IMPORTED_MODULE_2__.ICommentPanel, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    activate: (app, panel, shell) => {
        const commentRegistry = panel.commentRegistry;
        const commentWidgetRegistry = panel.commentWidgetRegistry;
        const editorTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: 'code-editor-wrappers'
        });
        commentRegistry.addFactory(new _commentfactory__WEBPACK_IMPORTED_MODULE_3__.TextSelectionCommentFactory());
        commentWidgetRegistry.addFactory(new _widgetfactory__WEBPACK_IMPORTED_MODULE_4__.TextSelectionCommentWidgetFactory({
            commentRegistry,
            tracker: editorTracker
        }));
        const button = panel.button;
        app.commands.addCommand(CommandIDs.addComment, {
            label: 'Add Comment',
            execute: () => {
                let editorWidget = shell.currentWidget
                    .content;
                if (editorWidget == null) {
                    return;
                }
                const model = panel.model;
                if (model == null) {
                    return;
                }
                const comments = model.comments;
                let index = comments.length;
                let { start, end } = editorWidget.editor.getSelection();
                //backwards selection compatibility
                if (start.line > end.line ||
                    (start.line === end.line && start.column > end.column)) {
                    [start, end] = [end, start];
                }
                for (let i = 0; i < comments.length; i++) {
                    const comment = comments.get(i);
                    let sel = comment.target;
                    let commentStart = sel.start;
                    if (start.line < commentStart.line ||
                        (start.line === commentStart.line &&
                            start.column <= commentStart.column)) {
                        index = i;
                        break;
                    }
                }
                panel.mockComment({
                    identity: (0,_api__WEBPACK_IMPORTED_MODULE_5__.getIdentity)(model.awareness),
                    type: 'text-selection',
                    source: editorWidget
                }, index);
            }
        });
        // Ideally, the button should be anchored to the CodeMirrorEditor and scroll along with it.
        // However, when using the scroll element as the anchor, click events first register on the
        // editor, causing the awareness to update and the button to close without triggering the click
        // callback. For now, scrolling causes the button to close instead.
        function openButton(x, y, anchor) {
            const onScroll = () => button.close();
            anchor.addEventListener('scroll', onScroll, {
                passive: true,
                once: true
            });
            button.open(x, y, () => {
                void app.commands.execute(CommandIDs.addComment);
                anchor.removeEventListener('scroll', onScroll);
            });
        }
        let currAwareness = null;
        let handler;
        let onMouseup;
        //commenting stuff for non-notebook/json files
        shell.currentChanged.connect(async (_, changed) => {
            if (currAwareness != null && handler != null && onMouseup != null) {
                document.removeEventListener('mouseup', onMouseup);
                currAwareness.off('change', handler);
                button.close();
            }
            if (changed.newValue == null /*|| panel.model == null*/) {
                return;
            }
            const editorWidget = Private.getEditor(changed.newValue);
            if (editorWidget == null) {
                return;
            }
            if (!editorTracker.has(editorWidget)) {
                await editorTracker.add(editorWidget);
            }
            editorWidget.node.focus();
            editorWidget.editor.focus();
            onMouseup = (_) => {
                const { right } = editorWidget.node.getBoundingClientRect();
                const { start, end } = editorWidget.editor.getSelection();
                const coord1 = editorWidget.editor.getCoordinateForPosition(start);
                const coord2 = editorWidget.editor.getCoordinateForPosition(end);
                const node = editorWidget.node.getElementsByClassName('CodeMirror-scroll')[0];
                openButton(right - 20, (coord1.top + coord2.bottom) / 2 - 10, node);
            };
            handler = () => {
                const { start, end } = editorWidget.editor.getSelection();
                if (start.column !== end.column || start.line !== end.line) {
                    document.addEventListener('mouseup', onMouseup, { once: true });
                }
                else {
                    button.close();
                }
            };
            if (currAwareness != null) {
                currAwareness.off('change', handler);
            }
            currAwareness = editorWidget.editor.model.sharedModel
                .awareness;
            currAwareness.on('change', handler);
        });
        app.contextMenu.addItem({
            command: CommandIDs.addComment,
            selector: '.jp-FileEditorCodeWrapper'
        });
    }
};
var Private;
(function (Private) {
    function getEditor(widget) {
        if (!widget.hasClass('jp-Document')) {
            return;
        }
        const content = widget.content;
        if (!content.hasClass('jp-FileEditor')) {
            return;
        }
        return content;
    }
    Private.getEditor = getEditor;
})(Private || (Private = {}));
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (textCommentingPlugin);


/***/ }),

/***/ "./lib/text/utils.js":
/*!***************************!*\
  !*** ./lib/text/utils.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "docFromWrapper": () => (/* binding */ docFromWrapper),
/* harmony export */   "markTextSelection": () => (/* binding */ markTextSelection)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/utils.js");

function docFromWrapper(wrapper) {
    return wrapper.editor.doc;
}
function markTextSelection(doc, comment) {
    const color = comment.identity.color;
    const r = parseInt(color.slice(1, 3), 16);
    const g = parseInt(color.slice(3, 5), 16);
    const b = parseInt(color.slice(5, 7), 16);
    const { start, end } = comment.target;
    const forward = start.line < end.line ||
        (start.line === end.line && start.column <= end.column);
    const anchor = (0,_api__WEBPACK_IMPORTED_MODULE_0__.toCodeMirrorPosition)(forward ? start : end);
    const head = (0,_api__WEBPACK_IMPORTED_MODULE_0__.toCodeMirrorPosition)(forward ? end : start);
    return doc.markText(anchor, head, {
        className: 'jc-Highlight',
        title: `${comment.identity.name}: ${(0,_api__WEBPACK_IMPORTED_MODULE_0__.truncate)(comment.text, 140)}`,
        css: `background-color: rgba( ${r}, ${g}, ${b}, 0.15)`,
        attributes: { id: `CommentMark-${comment.id}` }
    });
}


/***/ }),

/***/ "./lib/text/widget.js":
/*!****************************!*\
  !*** ./lib/text/widget.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TextSelectionCommentWidget": () => (/* binding */ TextSelectionCommentWidget)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/widget.js");
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../api */ "./lib/api/utils.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils */ "./lib/text/utils.js");


class TextSelectionCommentWidget extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidget {
    constructor(options) {
        super(options);
        this._mark = options.mark;
    }
    dispose() {
        this._mark.clear();
        super.dispose();
    }
    toJSON() {
        const json = super.toJSON();
        const mark = this._mark;
        if (mark == null) {
            console.warn('No mark found--serializing based on initial text selection position', this);
            return json;
        }
        const range = mark.find();
        if (range == null) {
            console.warn('Mark no longer exists in code editor--serializing based on initial text selection position', this);
            return json;
        }
        const textSelectionComment = json;
        const { from, to } = range;
        textSelectionComment.target.start = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeEditorPosition)(from);
        textSelectionComment.target.end = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeEditorPosition)(to);
        return textSelectionComment;
    }
    getPreview() {
        if (this.isMock || this._mark == null) {
            return Private.getMockCommentPreviewText(this._doc, this.comment);
        }
        const range = this._mark.find();
        if (range == null) {
            return '';
        }
        const { from, to } = range;
        const text = this._doc.getRange(from, to);
        return (0,_api__WEBPACK_IMPORTED_MODULE_1__.truncate)(text, 140);
    }
    get element() {
        var _a;
        return ((_a = document.getElementById(`CommentMark-${this.commentID}`)) !== null && _a !== void 0 ? _a : undefined);
    }
    get _doc() {
        return (0,_utils__WEBPACK_IMPORTED_MODULE_2__.docFromWrapper)(this.target);
    }
}
var Private;
(function (Private) {
    function getMockCommentPreviewText(doc, comment) {
        const { start, end } = comment.target;
        const forward = start.line < end.line ||
            (start.line === end.line && start.column <= end.column);
        const from = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeMirrorPosition)(forward ? start : end);
        const to = (0,_api__WEBPACK_IMPORTED_MODULE_1__.toCodeMirrorPosition)(forward ? end : start);
        const text = doc.getRange(from, to);
        return (0,_api__WEBPACK_IMPORTED_MODULE_1__.truncate)(text, 140);
    }
    Private.getMockCommentPreviewText = getMockCommentPreviewText;
})(Private || (Private = {}));


/***/ }),

/***/ "./lib/text/widgetfactory.js":
/*!***********************************!*\
  !*** ./lib/text/widgetfactory.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TextSelectionCommentWidgetFactory": () => (/* binding */ TextSelectionCommentWidgetFactory)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../api */ "./lib/api/factory.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./widget */ "./lib/text/widget.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./utils */ "./lib/text/utils.js");



class TextSelectionCommentWidgetFactory extends _api__WEBPACK_IMPORTED_MODULE_0__.CommentWidgetFactory {
    constructor(options) {
        super(options);
        this.commentType = 'text-selection';
        this.widgetType = 'text-selection';
        this._tracker = options.tracker;
    }
    createWidget(comment, model, target) {
        const wrapper = target !== null && target !== void 0 ? target : this._tracker.currentWidget;
        if (wrapper == null) {
            console.error('No CodeEditorWrapper found for comment', comment);
            return;
        }
        const mark = (0,_utils__WEBPACK_IMPORTED_MODULE_1__.markTextSelection)((0,_utils__WEBPACK_IMPORTED_MODULE_1__.docFromWrapper)(wrapper), comment);
        return new _widget__WEBPACK_IMPORTED_MODULE_2__.TextSelectionCommentWidget({
            comment,
            model,
            mark,
            target: wrapper
        });
    }
}


/***/ }),

/***/ "./style/icons/user-icon-0.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-0.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91,12,12,0,0,1,12.24,24h-.66A12,12,0,0,1,0,12,11.87,11.87,0,0,1,2.33,4.9,12,12,0,0,1,11,0c.35,0,.69,0,1,0A12,12,0,0,1,23.71,9.36a11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91,5.47,5.47,0,0,1,22.84,9.29a4.94,4.94,0,0,1,.87.07,11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3,3.6,3.6,0,1,1,1.76-7C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M12.24,24h-.66A21.81,21.81,0,0,0,8.93,12.15,21.63,21.63,0,0,0,2.33,4.9,12,12,0,0,1,11,0a11.67,11.67,0,0,1,.68,2A45.15,45.15,0,0,1,12.24,24Z\"/><circle class=\"cls-1\" cx=\"8.35\" cy=\"5.1\" r=\"2.86\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-1.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-1.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91a12,12,0,0,1-6,3.7,11.67,11.67,0,0,1-2.79.39h-.66A12,12,0,0,1,0,12a12.49,12.49,0,0,1,.14-1.85A11.54,11.54,0,0,1,.46,8.71,11.68,11.68,0,0,1,2.33,4.9,12,12,0,0,1,11,0c.35,0,.69,0,1,0A12,12,0,0,1,23.71,9.36,12.7,12.7,0,0,1,24,11.24v.1C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91a12,12,0,0,1-6,3.7A21.75,21.75,0,0,0,9.22,15,21.7,21.7,0,0,0,.14,10.15,11.54,11.54,0,0,1,.46,8.71c1.14.33,2.27.78,3.4,1.1a58.13,58.13,0,0,0,9.1,2,30,30,0,0,0,11-.54v.1C24,11.56,24,11.78,24,12Z\"/><circle class=\"cls-1\" cx=\"17.61\" cy=\"16.51\" r=\"2.62\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-10.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-10.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91,12,12,0,0,1,12.24,24h-.66a12.08,12.08,0,0,1-1.21-.1,12.31,12.31,0,0,1-2.1-.48A12,12,0,0,1,0,12,11.87,11.87,0,0,1,2.33,4.9v0A12,12,0,0,1,7.05,1.07a11.61,11.61,0,0,1,2-.71A13,13,0,0,1,11,0c.35,0,.69,0,1,0A12,12,0,0,1,23.71,9.36a11.66,11.66,0,0,1,.27,2v.05C24,11.59,24,11.8,24,12Z\"/><path class=\"cls-2\" d=\"M8,11.39A6.57,6.57,0,0,1,1.58,18,12,12,0,0,1,0,12,11.87,11.87,0,0,1,2.33,4.9v0A6.58,6.58,0,0,1,8,11.39Z\"/><path class=\"cls-2\" d=\"M24,11.39a4.19,4.19,0,0,1-2.89-7.22,12,12,0,0,1,2.62,5.19,11.66,11.66,0,0,1,.27,2Z\"/><path class=\"cls-2\" d=\"M9.08.36a11.61,11.61,0,0,0-2,.71A13.26,13.26,0,0,1,8.27,23.41a12.31,12.31,0,0,0,2.1.48A14.95,14.95,0,0,0,9.08.36Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-11.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-11.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3.71.71,0,0,1-.1.14A11.18,11.18,0,0,1,21,19.91a13.13,13.13,0,0,1-2,1.84A12,12,0,0,1,12.24,24h-.78a11.94,11.94,0,0,1-2.62-.41q-.43-.12-.84-.27A12.14,12.14,0,0,1,5.35,22,12,12,0,0,1,.92,7.38,12.2,12.2,0,0,1,5,2.22,12,12,0,0,1,11,0c.35,0,.69,0,1,0a11.85,11.85,0,0,1,6.22,1.74,11.71,11.71,0,0,1,2.31,1.83,11.74,11.74,0,0,1,3.18,5.79,9.88,9.88,0,0,1,.19,1.11,8,8,0,0,1,.08.87C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M20.53,3.57a11.71,11.71,0,0,0-2.31-1.83A23.43,23.43,0,0,0,5.35,22,12.14,12.14,0,0,0,8,23.31c0-.22,0-.44,0-.66A20.78,20.78,0,0,1,20.53,3.57Z\"/><path class=\"cls-2\" d=\"M23.71,9.36a12,12,0,0,0-.43-1.48A23.45,23.45,0,0,0,8.84,23.58a11.94,11.94,0,0,0,2.62.41A20.83,20.83,0,0,1,23.9,10.47,9.88,9.88,0,0,0,23.71,9.36Z\"/><path class=\"cls-2\" d=\"M6,4.56A3.32,3.32,0,0,1,2.67,7.88a3.28,3.28,0,0,1-1.75-.5A12.2,12.2,0,0,1,5,2.22,3.36,3.36,0,0,1,6,4.56Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-12.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-12.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09,12,12,0,0,0,12.24,0h-.66A12,12,0,0,0,0,12v.33A12,12,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,11.71-9.36,11.66,11.66,0,0,0,.27-2c0-.17,0-.34,0-.51Z\"/><path class=\"cls-2\" d=\"M24,12.15a5.74,5.74,0,1,0-5.09,9.66,12,12,0,0,0,4.8-7.17,11.66,11.66,0,0,0,.27-2C24,12.49,24,12.32,24,12.15Z\"/><path class=\"cls-2\" d=\"M6.32,8.59A4.27,4.27,0,0,0,2.73,4.38,12,12,0,0,0,0,12v.33a4.2,4.2,0,0,0,2.05.53A4.27,4.27,0,0,0,6.32,8.59Z\"/><circle class=\"cls-2\" cx=\"13.57\" cy=\"6.34\" r=\"2.33\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-13.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-13.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09,12,12,0,0,0,12.24,0h-.66a12.08,12.08,0,0,0-1.21.1,12.31,12.31,0,0,0-2.1.48A12,12,0,0,0,0,12a11.87,11.87,0,0,0,2.33,7.1v0a12,12,0,0,0,4.71,3.81,11.61,11.61,0,0,0,2,.71A13,13,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,11.71-9.36,11.66,11.66,0,0,0,.27-2v-.05C24,12.41,24,12.2,24,12Z\"/><path class=\"cls-2\" d=\"M8,12.61A6.57,6.57,0,0,0,1.58,6,12,12,0,0,0,0,12a11.87,11.87,0,0,0,2.33,7.1v0A6.58,6.58,0,0,0,8,12.61Z\"/><path class=\"cls-2\" d=\"M24,12.61a4.19,4.19,0,0,0-2.89,7.22,12,12,0,0,0,2.62-5.19,11.66,11.66,0,0,0,.27-2Z\"/><path class=\"cls-2\" d=\"M15.49,11.37A14.9,14.9,0,0,0,10.37.11a12.31,12.31,0,0,0-2.1.48A13.26,13.26,0,0,1,7.05,22.93a11.61,11.61,0,0,0,2,.71A14.9,14.9,0,0,0,15.49,11.37Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-14.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-14.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3.71.71,0,0,0-.1-.14A11.18,11.18,0,0,0,21,4.09a13.13,13.13,0,0,0-2-1.84A12,12,0,0,0,12.24,0h-.78A11.94,11.94,0,0,0,8.84.42Q8.41.54,8,.69A12.14,12.14,0,0,0,5.35,2,12,12,0,0,0,.92,16.62,12.2,12.2,0,0,0,5,21.78,12,12,0,0,0,11,24c.35,0,.69,0,1,0a11.85,11.85,0,0,0,6.22-1.74,11.71,11.71,0,0,0,2.31-1.83,11.74,11.74,0,0,0,3.18-5.79,9.88,9.88,0,0,0,.19-1.11,8,8,0,0,0,.08-.87C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M8,1.35c0-.22,0-.44,0-.66A12.14,12.14,0,0,0,5.35,2,23.43,23.43,0,0,0,18.22,22.26a11.71,11.71,0,0,0,2.31-1.83A20.78,20.78,0,0,1,8,1.35Z\"/><path class=\"cls-2\" d=\"M23.9,13.53A20.83,20.83,0,0,1,11.46,0,11.94,11.94,0,0,0,8.84.42a23.45,23.45,0,0,0,14.44,15.7,12,12,0,0,0,.43-1.48A9.88,9.88,0,0,0,23.9,13.53Z\"/><path class=\"cls-2\" d=\"M6,19.44a3.32,3.32,0,0,0-3.33-3.32,3.28,3.28,0,0,0-1.75.5A12.2,12.2,0,0,0,5,21.78,3.36,3.36,0,0,0,6,19.44Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-15.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-15.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M14.81.33A12.14,12.14,0,0,0,12.24,0h-.66A12,12,0,0,0,.41,15.13,16.81,16.81,0,0,0,14.81.33Z\"/><path class=\"cls-2\" d=\"M16.7,1A12.33,12.33,0,0,0,14.81.33,16.81,16.81,0,0,1,.41,15.13c.07.25.15.5.23.75A16.8,16.8,0,0,0,16.7,1Z\"/><circle class=\"cls-2\" cx=\"19.39\" cy=\"10.49\" r=\"2.19\"/><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09,12.08,12.08,0,0,0,16.7,1,16.8,16.8,0,0,1,.64,15.88,11.78,11.78,0,0,0,2.33,19.1,12,12,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,11.27-7.88c.05-.13.1-.26.14-.39.12-.36.21-.72.3-1.09a11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M23.27,16.12a6,6,0,0,0-9,7.67,12,12,0,0,0,9-7.67Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-16.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-16.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12.05,12.05,0,0,0-.14-1.81A11.91,11.91,0,0,0,21,4.09,12,12,0,0,0,12.24,0h-.66A13.16,13.16,0,0,0,10,.16,12,12,0,0,0,0,11.7V12a11.87,11.87,0,0,0,2.33,7.1,12.06,12.06,0,0,0,3.44,3.16h0A12.16,12.16,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,11.71-9.36,11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M8.21,17.39A6.09,6.09,0,0,0,0,11.7V12a11.87,11.87,0,0,0,2.33,7.1,12.06,12.06,0,0,0,3.44,3.16h0A6.08,6.08,0,0,0,8.21,17.39Z\"/><path class=\"cls-2\" d=\"M23.86,10.19A11.91,11.91,0,0,0,21,4.09,12,12,0,0,0,12.24,0h-.66A13.16,13.16,0,0,0,10,.16a8.83,8.83,0,0,0,8.22,12A8.78,8.78,0,0,0,23.86,10.19Z\"/><circle class=\"cls-2\" cx=\"11.53\" cy=\"19.25\" r=\"1.21\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-17.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-17.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a11.89,11.89,0,0,0-1.63-6h0l-.15-.26a.71.71,0,0,0-.1-.14A11.18,11.18,0,0,0,21,4.09a13.13,13.13,0,0,0-2-1.84A12,12,0,0,0,12.24,0h-.66A12,12,0,0,0,4.41,21.3,12,12,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,11.71-9.36,11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M22.37,6l-.15-.26a.71.71,0,0,0-.1-.14A11.18,11.18,0,0,0,21,4.09a13.13,13.13,0,0,0-2-1.84A12,12,0,0,0,12.24,0h-.66A12,12,0,0,0,3.8,3.24,17.18,17.18,0,0,1,6.09,9.82,22.89,22.89,0,0,1,4.41,21.3,12.33,12.33,0,0,0,7.26,23a7.86,7.86,0,0,0,.7-1.5c1.31-3.54,2-7.3,3.55-10.74a9,9,0,0,1,2.88-3.85A9.08,9.08,0,0,1,20,5.76C20.8,5.8,21.58,5.89,22.37,6Z\"/><circle class=\"cls-2\" cx=\"17.32\" cy=\"11.05\" r=\"2.94\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-18.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-18.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09a11.61,11.61,0,0,0-1.28-1.25A12,12,0,0,0,13.92.15,15.2,15.2,0,0,0,12.24,0h-.89A12,12,0,0,0,0,12a11.87,11.87,0,0,0,2.33,7.1,11.7,11.7,0,0,0,1.81,2l.41.34a12,12,0,0,0,5.62,2.45L11,24l.75,0H12a12,12,0,0,0,11.71-9.36,11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M19.75,2.84A12,12,0,0,0,13.92.15a13.09,13.09,0,0,0-4.66,3.1,19.44,19.44,0,0,0-4.85,11,40.31,40.31,0,0,0-.27,6.86l.41.34q.27-1.29.6-2.58c1.06-4.22,2.61-8.46,5.57-11.65A13.14,13.14,0,0,1,19.75,2.84Z\"/><circle class=\"cls-2\" cx=\"15.4\" cy=\"13.02\" r=\"3.15\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-19.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-19.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09,12,12,0,0,0,12.24,0h-.89A12,12,0,0,0,0,12,12,12,0,0,0,10.17,23.86L11,24l.75,0H12a12,12,0,0,0,11.71-9.36,11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M11.92.68A7.3,7.3,0,0,0,11.35,0,11.9,11.9,0,0,0,3.77,3.27,11.82,11.82,0,0,1,5.67,4a11.84,11.84,0,0,1,5.68,6.09,15.3,15.3,0,0,1,.29,9.76,26,26,0,0,1-1.47,4L11,24l.75,0a13.83,13.83,0,0,0,.82-1.23A20.54,20.54,0,0,0,15,14.58C15.58,9.74,14.93,4.51,11.92.68Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-2.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-2.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a11.92,11.92,0,0,1-1,4.86,11.67,11.67,0,0,1-.65,1.27l-.11.17a.67.67,0,0,1-.09.14A11.18,11.18,0,0,1,21,19.91a13.13,13.13,0,0,1-2,1.84A12,12,0,0,1,12.24,24h-.66A11.94,11.94,0,0,1,3.63,20.6a12.9,12.9,0,0,1-1-1.17,12,12,0,0,1-2.31-10A11.67,11.67,0,0,1,.73,7.87a12,12,0,0,1,1.6-3l.18-.24A11.94,11.94,0,0,1,11,.05c.31,0,.61,0,.92,0H12a12,12,0,0,1,5.69,1.43,12.69,12.69,0,0,1,1.11.68,12.07,12.07,0,0,1,4.91,7.25,12.76,12.76,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M18.05,6.63a13.61,13.61,0,0,1,.75-4.52,12.69,12.69,0,0,0-1.11-.68,15.51,15.51,0,0,0-.88,5.2,13.92,13.92,0,0,0,5.51,11.5A11.67,11.67,0,0,0,23,16.86,12.37,12.37,0,0,1,18.05,6.63Z\"/><path class=\"cls-2\" d=\"M.73,7.87A11.67,11.67,0,0,0,.27,9.46a13.13,13.13,0,0,1,2.47,7.82,15.22,15.22,0,0,1-.16,2.15,12.9,12.9,0,0,0,1,1.17A15.71,15.71,0,0,0,4,17.28,14.67,14.67,0,0,0,.73,7.87Z\"/><path class=\"cls-2\" d=\"M13.36,3.74a5.46,5.46,0,0,1-10.85.92A11.94,11.94,0,0,1,11,.05c.31,0,.61,0,.92,0A5.48,5.48,0,0,1,13.36,3.74Z\"/><circle class=\"cls-2\" cx=\"7.89\" cy=\"13.34\" r=\"2.19\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-20.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-20.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a11.89,11.89,0,0,0-1.63-6h0l-.15-.26a.71.71,0,0,0-.1-.14A11.18,11.18,0,0,0,21,4.09a13.13,13.13,0,0,0-2-1.84A12,12,0,0,0,12.24,0h-.66A11.69,11.69,0,0,0,9.27.32,12,12,0,0,0,2.33,19.1a12.06,12.06,0,0,0,2.08,2.2A12,12,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,9.83-5.12c.12-.17.24-.34.35-.52a2.39,2.39,0,0,1,.13-.21h0a3.62,3.62,0,0,0,.24-.43c.08-.14.16-.29.23-.44l.11-.21,0-.07.18-.41.18-.47,0-.09a12.85,12.85,0,0,0,.4-1.38,11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><circle class=\"cls-2\" cx=\"20.96\" cy=\"10.22\" r=\"1.41\"/><path class=\"cls-2\" d=\"M11.33,4.5A5.27,5.27,0,0,0,9.27.32a12,12,0,0,0-8,6.36A5.28,5.28,0,0,0,11.33,4.5Z\"/><path class=\"cls-2\" d=\"M17.32,9.15a12.46,12.46,0,0,1,2-6.64L19,2.26A12.57,12.57,0,0,0,17,1.1,16.86,16.86,0,0,0,14.17,8c-.48,2.43-.58,5.09.65,7.24a7.49,7.49,0,0,0,5.61,3.56,8.32,8.32,0,0,0,1.41.06A12.09,12.09,0,0,0,23.31,16a5.8,5.8,0,0,1-4.17-1.61A7.32,7.32,0,0,1,17.32,9.15Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-21.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-21.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09,12,12,0,0,0,12.24,0h-.66A12,12,0,0,0,0,12a11.87,11.87,0,0,0,2.33,7.1A12,12,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,11.71-9.36,11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09a5.47,5.47,0,0,0,1.81,10.62,4.94,4.94,0,0,0,.87-.07,11.66,11.66,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3,3.6,3.6,0,1,0,1.76,7C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M12.24,0h-.66A21.81,21.81,0,0,1,8.93,11.85a21.63,21.63,0,0,1-6.6,7.25A12,12,0,0,0,11,24a11.67,11.67,0,0,0,.68-2A45.15,45.15,0,0,0,12.24,0Z\"/><circle class=\"cls-1\" cx=\"8.35\" cy=\"18.9\" r=\"2.86\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-22.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-22.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09a12,12,0,0,0-6-3.7A11.67,11.67,0,0,0,12.24,0h-.66A12,12,0,0,0,0,12a12.49,12.49,0,0,0,.14,1.85,11.54,11.54,0,0,0,.32,1.44A11.68,11.68,0,0,0,2.33,19.1,12,12,0,0,0,11,24c.35,0,.69,0,1,0a12,12,0,0,0,11.71-9.36A12.7,12.7,0,0,0,24,12.76v-.1C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M24,12a12,12,0,0,0-1.78-6.3A11.74,11.74,0,0,0,21,4.09a12,12,0,0,0-6-3.7A21.75,21.75,0,0,1,9.22,9,21.7,21.7,0,0,1,.14,13.85a11.54,11.54,0,0,0,.32,1.44c1.14-.33,2.27-.78,3.4-1.1a58.13,58.13,0,0,1,9.1-2,30,30,0,0,1,11,.54v-.1C24,12.44,24,12.22,24,12Z\"/><circle class=\"cls-1\" cx=\"17.61\" cy=\"7.49\" r=\"2.62\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-23.svg":
/*!**************************************!*\
  !*** ./style/icons/user-icon-23.svg ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a11.92,11.92,0,0,0-1-4.86,11.67,11.67,0,0,0-.65-1.27l-.11-.17a.67.67,0,0,0-.09-.14A11.18,11.18,0,0,0,21,4.09a13.13,13.13,0,0,0-2-1.84A12,12,0,0,0,12.24,0h-.66A11.94,11.94,0,0,0,3.63,3.4a12.9,12.9,0,0,0-1,1.17,12,12,0,0,0-2.31,10,11.67,11.67,0,0,0,.46,1.59,12,12,0,0,0,1.6,3l.18.24A11.94,11.94,0,0,0,11,24c.31,0,.61.05.92.05H12a12,12,0,0,0,5.69-1.43,12.69,12.69,0,0,0,1.11-.68,12.07,12.07,0,0,0,4.91-7.25,12.76,12.76,0,0,0,.27-2C24,12.44,24,12.22,24,12Z\"/><path class=\"cls-2\" d=\"M23,7.14a11.67,11.67,0,0,0-.65-1.27,13.92,13.92,0,0,0-5.51,11.5,15.51,15.51,0,0,0,.88,5.2,12.69,12.69,0,0,0,1.11-.68,13.61,13.61,0,0,1-.75-4.52A12.37,12.37,0,0,1,23,7.14Z\"/><path class=\"cls-2\" d=\"M4,6.72A15.71,15.71,0,0,0,3.63,3.4a12.9,12.9,0,0,0-1,1.17,15.22,15.22,0,0,1,.16,2.15A13.13,13.13,0,0,1,.27,14.54a11.67,11.67,0,0,0,.46,1.59A14.67,14.67,0,0,0,4,6.72Z\"/><path class=\"cls-2\" d=\"M13.36,20.26a5.46,5.46,0,0,0-10.85-.92A11.94,11.94,0,0,0,11,24c.31,0,.61.05.92.05A5.48,5.48,0,0,0,13.36,20.26Z\"/><circle class=\"cls-2\" cx=\"7.89\" cy=\"10.66\" r=\"2.19\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-3.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-3.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91a11.61,11.61,0,0,1-1.28,1.25,12,12,0,0,1-5.83,2.69,15.2,15.2,0,0,1-1.68.15h-.89A12,12,0,0,1,0,12,11.87,11.87,0,0,1,2.33,4.9a11.7,11.7,0,0,1,1.81-2l.41-.34A12,12,0,0,1,10.17.14L11,0l.75,0H12A12,12,0,0,1,23.71,9.36a11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M19.75,21.16a12,12,0,0,1-5.83,2.69,13.09,13.09,0,0,1-4.66-3.1,19.44,19.44,0,0,1-4.85-11,40.31,40.31,0,0,1-.27-6.86l.41-.34q.27,1.29.6,2.58c1.06,4.22,2.61,8.46,5.57,11.65A13.14,13.14,0,0,0,19.75,21.16Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-4.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-4.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91,12,12,0,0,1,12.24,24h-.89A12,12,0,0,1,0,12,12,12,0,0,1,10.17.14L11,0l.75,0H12A12,12,0,0,1,23.71,9.36a11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M11.92,23.32a7.3,7.3,0,0,1-.57.66,11.9,11.9,0,0,1-7.58-3.25A11.82,11.82,0,0,0,5.67,20a11.84,11.84,0,0,0,5.68-6.09,15.3,15.3,0,0,0,.29-9.76,26,26,0,0,0-1.47-4L11,0l.75,0a13.83,13.83,0,0,1,.82,1.23A20.54,20.54,0,0,1,15,9.42C15.58,14.26,14.93,19.49,11.92,23.32Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-5.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-5.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a11.89,11.89,0,0,1-1.63,6h0l-.15.26a.71.71,0,0,1-.1.14A11.18,11.18,0,0,1,21,19.91a13.13,13.13,0,0,1-2,1.84A12,12,0,0,1,12.24,24h-.66a11.69,11.69,0,0,1-2.31-.31A12,12,0,0,1,2.33,4.9,12.06,12.06,0,0,1,4.41,2.7,12,12,0,0,1,11,0c.35,0,.69,0,1,0a12,12,0,0,1,9.83,5.12c.12.17.24.34.35.52a2.39,2.39,0,0,0,.13.21h0a3.62,3.62,0,0,1,.24.43c.08.14.16.29.23.44l.11.21,0,.07.18.41.18.47,0,.09a12.85,12.85,0,0,1,.4,1.38,11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><circle class=\"cls-2\" cx=\"20.96\" cy=\"13.78\" r=\"1.41\"/><path class=\"cls-2\" d=\"M11.33,19.5a5.27,5.27,0,0,1-2.06,4.18,12,12,0,0,1-8-6.36A5.28,5.28,0,0,1,11.33,19.5Z\"/><path class=\"cls-2\" d=\"M17.32,14.85a12.46,12.46,0,0,0,2,6.64l-.33.25a12.57,12.57,0,0,1-2,1.16A16.86,16.86,0,0,1,14.17,16c-.48-2.43-.58-5.09.65-7.24a7.49,7.49,0,0,1,5.61-3.56,8.32,8.32,0,0,1,1.41-.06A12.09,12.09,0,0,1,23.31,8a5.8,5.8,0,0,0-4.17,1.61A7.32,7.32,0,0,0,17.32,14.85Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-6.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-6.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M14.81,23.67a12.14,12.14,0,0,1-2.57.33h-.66A12,12,0,0,1,.41,8.87,16.81,16.81,0,0,1,14.81,23.67Z\"/><path class=\"cls-2\" d=\"M16.7,23a12.33,12.33,0,0,1-1.89.63A16.81,16.81,0,0,0,.41,8.87c.07-.25.15-.5.23-.75A16.8,16.8,0,0,1,16.7,23Z\"/><circle class=\"cls-2\" cx=\"19.39\" cy=\"13.51\" r=\"2.19\"/><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91,12.08,12.08,0,0,1,16.7,23,16.8,16.8,0,0,0,.64,8.12,11.78,11.78,0,0,1,2.33,4.9,12,12,0,0,1,11,0c.35,0,.69,0,1,0A12,12,0,0,1,23.27,7.88c.05.13.1.26.14.39.12.36.21.72.3,1.09a11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M23.27,7.88A6,6,0,0,1,19.4,9.29,6,6,0,0,1,14.25.21a12,12,0,0,1,9,7.67Z\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-7.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-7.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12.05,12.05,0,0,1-.14,1.81A11.91,11.91,0,0,1,21,19.91,12,12,0,0,1,12.24,24h-.66A13.16,13.16,0,0,1,10,23.84,12,12,0,0,1,0,12.3V12A11.87,11.87,0,0,1,2.33,4.9,12.06,12.06,0,0,1,5.77,1.74h0A12.16,12.16,0,0,1,11,0c.35,0,.69,0,1,0A12,12,0,0,1,23.71,9.36a11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M8.21,6.61A6.09,6.09,0,0,1,0,12.3V12A11.87,11.87,0,0,1,2.33,4.9,12.06,12.06,0,0,1,5.77,1.74h0A6.08,6.08,0,0,1,8.21,6.61Z\"/><path class=\"cls-2\" d=\"M23.86,13.81A11.91,11.91,0,0,1,21,19.91,12,12,0,0,1,12.24,24h-.66A13.16,13.16,0,0,1,10,23.84a8.83,8.83,0,0,1,13.82-10Z\"/><circle class=\"cls-2\" cx=\"18.26\" cy=\"7.36\" r=\"1.21\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-8.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-8.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a11.89,11.89,0,0,1-1.63,6h0l-.15.26a.71.71,0,0,1-.1.14A11.18,11.18,0,0,1,21,19.91a13.13,13.13,0,0,1-2,1.84A12,12,0,0,1,12.24,24h-.66A12,12,0,0,1,4.41,2.7,12,12,0,0,1,11,0c.35,0,.69,0,1,0A12,12,0,0,1,23.71,9.36a11.66,11.66,0,0,1,.27,2C24,11.56,24,11.78,24,12Z\"/><path class=\"cls-2\" d=\"M22.37,18l-.15.26a.71.71,0,0,1-.1.14A11.18,11.18,0,0,1,21,19.91a13.13,13.13,0,0,1-2,1.84A12,12,0,0,1,12.24,24h-.66A12,12,0,0,1,3.8,20.76a17.18,17.18,0,0,0,2.29-6.58A22.89,22.89,0,0,0,4.41,2.7,12.33,12.33,0,0,1,7.26,1,7.86,7.86,0,0,1,8,2.47C9.27,6,10,9.77,11.51,13.21a9,9,0,0,0,2.88,3.85A9.08,9.08,0,0,0,20,18.24C20.8,18.2,21.58,18.11,22.37,18Z\"/><circle class=\"cls-2\" cx=\"17.32\" cy=\"12.95\" r=\"2.94\"/></g></svg>");

/***/ }),

/***/ "./style/icons/user-icon-9.svg":
/*!*************************************!*\
  !*** ./style/icons/user-icon-9.svg ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><defs><style>.cls-1{fill:#282828;}.cls-2{fill:#fff;}</style></defs><g id=\"Layer_2\" data-name=\"Layer 2\"><path class=\"cls-1\" d=\"M24,12a12,12,0,0,1-1.78,6.3A11.74,11.74,0,0,1,21,19.91,12,12,0,0,1,12.24,24h-.66A12,12,0,0,1,0,12v-.33A12,12,0,0,1,11,0c.35,0,.69,0,1,0A12,12,0,0,1,23.71,9.36a11.66,11.66,0,0,1,.27,2c0,.17,0,.34,0,.51Z\"/><path class=\"cls-2\" d=\"M24,11.85a5.74,5.74,0,1,1-5.09-9.66,12,12,0,0,1,4.8,7.17,11.66,11.66,0,0,1,.27,2C24,11.51,24,11.68,24,11.85Z\"/><path class=\"cls-2\" d=\"M6.32,15.41a4.27,4.27,0,0,1-3.59,4.21A12,12,0,0,1,0,12v-.33a4.2,4.2,0,0,1,2.05-.53A4.27,4.27,0,0,1,6.32,15.41Z\"/><circle class=\"cls-2\" cx=\"13.57\" cy=\"17.66\" r=\"2.33\"/></g></svg>");

/***/ })

}]);
//# sourceMappingURL=lib_index_js.c101d033013e7879262f.js.map