(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory(require("react"));
	else if(typeof define === 'function' && define.amd)
		define(["react"], factory);
	else if(typeof exports === 'object')
		exports["dazzler_extra"] = factory(require("react"));
	else
		root["dazzler_extra"] = factory(root["React"]);
})(self, function(__WEBPACK_EXTERNAL_MODULE_react__) {
return (self["webpackChunkdazzler_name_"] = self["webpackChunkdazzler_name_"] || []).push([["extra"],{

/***/ "./src/extra/scss/index.scss":
/*!***********************************!*\
  !*** ./src/extra/scss/index.scss ***!
  \***********************************/
/***/ (() => {

// extracted by mini-css-extract-plugin

/***/ }),

/***/ "./src/extra/js/components/Drawer.tsx":
/*!********************************************!*\
  !*** ./src/extra/js/components/Drawer.tsx ***!
  \********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var Caret = function (_a) {
    var side = _a.side, opened = _a.opened;
    switch (side) {
        case 'top':
            return opened ? react_1["default"].createElement("span", null, "\u25B2") : react_1["default"].createElement("span", null, "\u25BC");
        case 'right':
            return opened ? react_1["default"].createElement("span", null, "\u25B8") : react_1["default"].createElement("span", null, "\u25C2");
        case 'left':
            return opened ? react_1["default"].createElement("span", null, "\u25C2") : react_1["default"].createElement("span", null, "\u25B8");
        case 'bottom':
            return opened ? react_1["default"].createElement("span", null, "\u25BC") : react_1["default"].createElement("span", null, "\u25B2");
        default:
            return null;
    }
};
/**
 * Draw content from the sides of the screen.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-drawer``
 *     - ``drawer-content``
 *     - ``drawer-control``
 *     - ``vertical``
 *     - ``horizontal``
 *     - ``right``
 *     - ``bottom``
 */
var Drawer = function (props) {
    var class_name = props.class_name, identity = props.identity, style = props.style, children = props.children, opened = props.opened, side = props.side, updateAspects = props.updateAspects;
    var css = [side];
    if (side === 'top' || side === 'bottom') {
        css.push('horizontal');
    }
    else {
        css.push('vertical');
    }
    return (react_1["default"].createElement("div", { className: ramda_1.join(' ', ramda_1.concat(css, [class_name])), id: identity, style: style },
        opened && (react_1["default"].createElement("div", { className: ramda_1.join(' ', ramda_1.concat(css, ['drawer-content'])) }, children)),
        react_1["default"].createElement("div", { className: ramda_1.join(' ', ramda_1.concat(css, ['drawer-control'])), onClick: function () { return updateAspects({ opened: !opened }); } },
            react_1["default"].createElement(Caret, { opened: opened, side: side }))));
};
Drawer.defaultProps = {
    side: 'top',
};
exports.default = Drawer;


/***/ }),

/***/ "./src/extra/js/components/Notice.tsx":
/*!********************************************!*\
  !*** ./src/extra/js/components/Notice.tsx ***!
  \********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var commons_1 = __webpack_require__(/*! commons */ "./src/commons/js/index.ts");
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
/**
 * Browser notifications with permissions handling.
 */
var Notice = /** @class */ (function (_super) {
    __extends(Notice, _super);
    function Notice(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            lastMessage: props.body,
            notification: null,
        };
        _this.onPermission = _this.onPermission.bind(_this);
        return _this;
    }
    Notice.prototype.componentDidMount = function () {
        var updateAspects = this.props.updateAspects;
        if (!('Notification' in window) && updateAspects) {
            updateAspects({ permission: 'unsupported' });
        }
        else if (Notification.permission === 'default') {
            Notification.requestPermission().then(this.onPermission);
        }
        else {
            this.onPermission(window.Notification.permission);
        }
    };
    Notice.prototype.componentDidUpdate = function (prevProps) {
        if (!prevProps.displayed && this.props.displayed) {
            this.sendNotification(this.props.permission);
        }
    };
    Notice.prototype.sendNotification = function (permission) {
        var _this = this;
        var _a = this.props, updateAspects = _a.updateAspects, body = _a.body, title = _a.title, icon = _a.icon, require_interaction = _a.require_interaction, lang = _a.lang, badge = _a.badge, tag = _a.tag, image = _a.image, vibrate = _a.vibrate;
        if (permission === 'granted') {
            var options = {
                requireInteraction: require_interaction,
                body: body,
                icon: icon,
                lang: lang,
                badge: badge,
                tag: tag,
                image: image,
                vibrate: vibrate,
            };
            var notification = new Notification(title, options);
            notification.onclick = function () {
                if (updateAspects) {
                    updateAspects(ramda_1.merge({ displayed: false }, commons_1.timestampProp('clicks', _this.props.clicks + 1)));
                }
            };
            notification.onclose = function () {
                if (updateAspects) {
                    updateAspects(ramda_1.merge({ displayed: false }, commons_1.timestampProp('closes', _this.props.closes + 1)));
                }
            };
        }
    };
    Notice.prototype.onPermission = function (permission) {
        var _a = this.props, displayed = _a.displayed, updateAspects = _a.updateAspects;
        if (updateAspects) {
            updateAspects({ permission: permission });
        }
        if (displayed) {
            this.sendNotification(permission);
        }
    };
    Notice.prototype.render = function () {
        return null;
    };
    return Notice;
}(react_1["default"].Component));
exports.default = Notice;


/***/ }),

/***/ "./src/extra/js/components/PageMap.tsx":
/*!*********************************************!*\
  !*** ./src/extra/js/components/PageMap.tsx ***!
  \*********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
/**
 * List of links to other page in the app.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-page-map``
 */
var PageMap = function (props) {
    var class_name = props.class_name, style = props.style, identity = props.identity;
    var _a = react_1.useState(null), pageMap = _a[0], setPageMap = _a[1];
    react_1.useEffect(function () {
        // @ts-ignore
        fetch(window.dazzler_base_url + "/dazzler/page-map").then(function (rep) {
            return rep.json().then(setPageMap);
        });
    }, []);
    return (react_1["default"].createElement("ul", { className: class_name, style: style, id: identity }, pageMap &&
        pageMap.map(function (page) { return (react_1["default"].createElement("li", { key: page.name },
            react_1["default"].createElement("a", { href: page.url }, page.title))); })));
};
PageMap.defaultProps = {};
exports.default = PageMap;


/***/ }),

/***/ "./src/extra/js/components/Pager.tsx":
/*!*******************************************!*\
  !*** ./src/extra/js/components/Pager.tsx ***!
  \*******************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var startOffset = function (page, itemPerPage) {
    return (page - 1) * (page > 1 ? itemPerPage : 0);
};
var endOffset = function (start, itemPerPage, page, total, leftOver) {
    return page !== total
        ? start + itemPerPage
        : leftOver !== 0
            ? start + leftOver
            : start + itemPerPage;
};
var showList = function (page, total, n) {
    if (total > n) {
        var middle = n / 2;
        var first = page >= total - middle
            ? total - n + 1
            : page > middle
                ? page - middle
                : 1;
        var last = page < total - middle ? first + n : total + 1;
        return ramda_1.range(first, last);
    }
    return ramda_1.range(1, total + 1);
};
var Page = function (_a) {
    var style = _a.style, class_name = _a.class_name, on_change = _a.on_change, text = _a.text, page = _a.page;
    return (react_1["default"].createElement("span", { style: style, className: class_name, onClick: function () { return on_change(page); } }, text || page));
};
/**
 * Paging for dazzler apps.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-pager``
 *     - ``page``
 */
var Pager = /** @class */ (function (_super) {
    __extends(Pager, _super);
    function Pager(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            current_page: null,
            start_offset: null,
            end_offset: null,
            pages: [],
            total_pages: Math.ceil(props.total_items / props.items_per_page),
        };
        _this.onChangePage = _this.onChangePage.bind(_this);
        return _this;
    }
    Pager.prototype.UNSAFE_componentWillMount = function () {
        this.onChangePage(this.props.current_page);
    };
    Pager.prototype.onChangePage = function (page) {
        var _a = this.props, items_per_page = _a.items_per_page, total_items = _a.total_items, updateAspects = _a.updateAspects, pages_displayed = _a.pages_displayed;
        var total_pages = this.state.total_pages;
        var start_offset = startOffset(page, items_per_page);
        var leftOver = total_items % items_per_page;
        var end_offset = endOffset(start_offset, items_per_page, page, total_pages, leftOver);
        var payload = {
            current_page: page,
            start_offset: start_offset,
            end_offset: end_offset,
            pages: showList(page, total_pages, pages_displayed),
        };
        this.setState(payload);
        if (updateAspects) {
            if (this.state.total_pages !== this.props.total_pages) {
                payload.total_pages = this.state.total_pages;
            }
            updateAspects(payload);
        }
    };
    Pager.prototype.UNSAFE_componentWillReceiveProps = function (props) {
        if (props.current_page !== this.state.current_page) {
            this.onChangePage(props.current_page);
        }
    };
    Pager.prototype.render = function () {
        var _this = this;
        var _a = this.state, current_page = _a.current_page, pages = _a.pages, total_pages = _a.total_pages;
        var _b = this.props, class_name = _b.class_name, identity = _b.identity, page_style = _b.page_style, page_class_name = _b.page_class_name;
        var css = ['page'];
        if (page_class_name) {
            css.push(page_class_name);
        }
        var pageCss = ramda_1.join(' ', css);
        return (react_1["default"].createElement("div", { className: class_name, id: identity },
            current_page > 1 && (react_1["default"].createElement(Page, { page: 1, text: 'first', style: page_style, class_name: pageCss, on_change: this.onChangePage })),
            current_page > 1 && (react_1["default"].createElement(Page, { page: current_page - 1, text: 'previous', style: page_style, class_name: pageCss, on_change: this.onChangePage })),
            pages.map(function (e) { return (react_1["default"].createElement(Page, { page: e, key: "page-" + e, style: page_style, class_name: pageCss, on_change: _this.onChangePage })); }),
            current_page < total_pages && (react_1["default"].createElement(Page, { page: current_page + 1, text: 'next', style: page_style, class_name: pageCss, on_change: this.onChangePage })),
            current_page < total_pages && (react_1["default"].createElement(Page, { page: total_pages, text: 'last', style: page_style, class_name: pageCss, on_change: this.onChangePage }))));
    };
    Pager.defaultProps = {
        current_page: 1,
        items_per_page: 10,
        pages_displayed: 10,
    };
    return Pager;
}(react_1["default"].Component));
exports.default = Pager;


/***/ }),

/***/ "./src/extra/js/components/PopUp.tsx":
/*!*******************************************!*\
  !*** ./src/extra/js/components/PopUp.tsx ***!
  \*******************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
function getMouseX(e, popup) {
    return (e.clientX -
        e.target.getBoundingClientRect().left -
        popup.getBoundingClientRect().width / 2);
}
/**
 * Wraps a component/text to render a popup when hovering
 * over the children or clicking on it.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-pop-up``
 *     - ``popup-content``
 *     - ``visible``
 */
var PopUp = /** @class */ (function (_super) {
    __extends(PopUp, _super);
    function PopUp(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            pos: null,
        };
        return _this;
    }
    PopUp.prototype.render = function () {
        var _this = this;
        var _a = this.props, class_name = _a.class_name, style = _a.style, identity = _a.identity, children = _a.children, content = _a.content, mode = _a.mode, updateAspects = _a.updateAspects, active = _a.active, content_style = _a.content_style, children_style = _a.children_style;
        return (react_1["default"].createElement("div", { className: class_name, style: style, id: identity },
            react_1["default"].createElement("div", { className: 'popup-content' + (active ? ' visible' : ''), style: __assign(__assign({}, (content_style || {})), { left: this.state.pos || 0 }), ref: function (r) { return (_this.popupRef = r); } }, content),
            react_1["default"].createElement("div", { className: "popup-children", onMouseEnter: function (e) {
                    if (mode === 'hover') {
                        _this.setState({ pos: getMouseX(e, _this.popupRef) }, function () { return updateAspects({ active: true }); });
                    }
                }, onMouseLeave: function () {
                    return mode === 'hover' && updateAspects({ active: false });
                }, onClick: function (e) {
                    if (mode === 'click') {
                        _this.setState({ pos: getMouseX(e, _this.popupRef) }, function () { return updateAspects({ active: !active }); });
                    }
                }, style: children_style }, children)));
    };
    PopUp.defaultProps = {
        mode: 'hover',
        active: false,
    };
    return PopUp;
}(react_1["default"].Component));
exports.default = PopUp;


/***/ }),

/***/ "./src/extra/js/components/Spinner.tsx":
/*!*********************************************!*\
  !*** ./src/extra/js/components/Spinner.tsx ***!
  \*********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
/**
 * Simple html/css spinner.
 */
var Spinner = function (props) {
    var class_name = props.class_name, style = props.style, identity = props.identity;
    return react_1["default"].createElement("div", { id: identity, className: class_name, style: style });
};
exports.default = Spinner;


/***/ }),

/***/ "./src/extra/js/components/Sticky.tsx":
/*!********************************************!*\
  !*** ./src/extra/js/components/Sticky.tsx ***!
  \********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
/**
 * A shorthand component for a sticky div.
 */
var Sticky = function (props) {
    var class_name = props.class_name, identity = props.identity, style = props.style, children = props.children, top = props.top, left = props.left, right = props.right, bottom = props.bottom;
    var styles = ramda_1.mergeAll([style, { top: top, left: left, right: right, bottom: bottom }]);
    return (react_1["default"].createElement("div", { className: class_name, id: identity, style: styles }, children));
};
exports.default = Sticky;


/***/ }),

/***/ "./src/extra/js/components/Toast.tsx":
/*!*******************************************!*\
  !*** ./src/extra/js/components/Toast.tsx ***!
  \*******************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
/**
 * Display a message over the ui that will disappears after a delay.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-toast``
 *     - ``opened``
 *     - ``toast-inner``
 *     - ``top``
 *     - ``top-left``
 *     - ``top-right``
 *     - ``bottom``
 *     - ``bottom-left``
 *     - ``bottom-right``
 *     - ``right``
 */
var Toast = function (props) {
    var class_name = props.class_name, style = props.style, identity = props.identity, message = props.message, position = props.position, opened = props.opened, delay = props.delay, updateAspects = props.updateAspects;
    var _a = react_1.useState(false), displayed = _a[0], setDisplayed = _a[1];
    var css = react_1.useMemo(function () {
        var c = [class_name, position];
        if (opened) {
            c.push('opened');
        }
        return ramda_1.join(' ', c);
    }, [class_name, opened, position]);
    react_1.useEffect(function () {
        if (opened && !displayed) {
            setTimeout(function () {
                updateAspects({ opened: false });
                setDisplayed(false);
            }, delay);
            setDisplayed(true);
        }
    }, [opened, displayed, delay]);
    return (react_1["default"].createElement("div", { className: css, style: style, id: identity }, message));
};
Toast.defaultProps = {
    delay: 3000,
    position: 'top',
    opened: true,
};
exports.default = Toast;


/***/ }),

/***/ "./src/extra/js/components/TreeView.tsx":
/*!**********************************************!*\
  !*** ./src/extra/js/components/TreeView.tsx ***!
  \**********************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var TreeViewElement = function (_a) {
    var label = _a.label, onClick = _a.onClick, identifier = _a.identifier, items = _a.items, level = _a.level, selected = _a.selected, expanded_items = _a.expanded_items, nest_icon_expanded = _a.nest_icon_expanded, nest_icon_collapsed = _a.nest_icon_collapsed;
    var isSelected = react_1.useMemo(function () { return selected && ramda_1.includes(identifier, selected); }, [selected, identifier]);
    var isExpanded = react_1.useMemo(function () { return ramda_1.includes(identifier, expanded_items); }, [expanded_items, expanded_items]);
    var css = ['tree-item-label', "level-" + level];
    if (isSelected) {
        css.push('selected');
    }
    return (react_1["default"].createElement("div", { className: "tree-item level-" + level, style: { marginLeft: level + "rem" } },
        react_1["default"].createElement("div", { className: ramda_1.join(' ', css), onClick: function (e) { return onClick(e, identifier, Boolean(items)); } },
            items && (react_1["default"].createElement("span", { className: "tree-caret" }, isExpanded ? nest_icon_expanded : nest_icon_collapsed)),
            label || identifier),
        items && isExpanded && (react_1["default"].createElement("div", { className: "tree-sub-items" }, items.map(function (item) {
            return renderItem({
                parent: identifier,
                onClick: onClick,
                item: item,
                level: level + 1,
                selected: selected,
                nest_icon_expanded: nest_icon_expanded,
                nest_icon_collapsed: nest_icon_collapsed,
                expanded_items: expanded_items,
            });
        })))));
};
var renderItem = function (_a) {
    var parent = _a.parent, item = _a.item, level = _a.level, rest = __rest(_a, ["parent", "item", "level"]);
    if (ramda_1.is(String, item)) {
        return (react_1["default"].createElement(TreeViewElement, __assign({ label: item, identifier: parent ? ramda_1.join('.', [parent, item]) : item, level: level || 0, key: item }, rest)));
    }
    return (react_1["default"].createElement(TreeViewElement, __assign({}, item, { level: level || 0, key: item.identifier, identifier: parent ? ramda_1.join('.', [parent, item.identifier]) : item.identifier }, rest)));
};
/**
 * A tree of nested items.
 *
 * :CSS:
 *
 *     - ``dazzler-extra-tree-view``
 *     - ``tree-item``
 *     - ``tree-item-label``
 *     - ``tree-sub-items``
 *     - ``tree-caret``
 *     - ``selected``
 *     - ``level-{n}``
 *
 * :example:
 *
 * .. literalinclude:: ../../tests/components/pages/treeview.py
 */
var TreeView = function (_a) {
    var class_name = _a.class_name, style = _a.style, identity = _a.identity, updateAspects = _a.updateAspects, items = _a.items, selected = _a.selected, expanded_items = _a.expanded_items, nest_icon_expanded = _a.nest_icon_expanded, nest_icon_collapsed = _a.nest_icon_collapsed;
    var onClick = function (e, identifier, expand) {
        e.stopPropagation();
        var payload = {};
        if (selected && ramda_1.includes(identifier, selected)) {
            var last = ramda_1.split('.', identifier);
            last = ramda_1.slice(0, last.length - 1, last);
            if (last.length === 0) {
                payload.selected = null;
            }
            else if (last.length === 1) {
                payload.selected = last[0];
            }
            else {
                payload.selected = ramda_1.join('.', last);
            }
        }
        else {
            payload.selected = identifier;
        }
        if (expand) {
            if (ramda_1.includes(identifier, expanded_items)) {
                payload.expanded_items = ramda_1.without([identifier], expanded_items);
            }
            else {
                payload.expanded_items = ramda_1.concat(expanded_items, [identifier]);
            }
        }
        updateAspects(payload);
    };
    return (react_1["default"].createElement("div", { className: class_name, style: style, id: identity }, items.map(function (item) {
        return renderItem({
            item: item,
            onClick: onClick,
            selected: selected,
            nest_icon_expanded: nest_icon_expanded,
            nest_icon_collapsed: nest_icon_collapsed,
            expanded_items: expanded_items,
        });
    })));
};
TreeView.defaultProps = {
    nest_icon_collapsed: '⏵',
    nest_icon_expanded: '⏷',
    expanded_items: [],
};
exports.default = TreeView;


/***/ }),

/***/ "./src/extra/js/index.ts":
/*!*******************************!*\
  !*** ./src/extra/js/index.ts ***!
  \*******************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
exports.PageMap = exports.Toast = exports.TreeView = exports.PopUp = exports.Drawer = exports.Sticky = exports.Spinner = exports.Pager = exports.Notice = void 0;
__webpack_require__(/*! ../scss/index.scss */ "./src/extra/scss/index.scss");
var Notice_1 = __importDefault(__webpack_require__(/*! ./components/Notice */ "./src/extra/js/components/Notice.tsx"));
exports.Notice = Notice_1["default"];
var Pager_1 = __importDefault(__webpack_require__(/*! ./components/Pager */ "./src/extra/js/components/Pager.tsx"));
exports.Pager = Pager_1["default"];
var Spinner_1 = __importDefault(__webpack_require__(/*! ./components/Spinner */ "./src/extra/js/components/Spinner.tsx"));
exports.Spinner = Spinner_1["default"];
var Sticky_1 = __importDefault(__webpack_require__(/*! ./components/Sticky */ "./src/extra/js/components/Sticky.tsx"));
exports.Sticky = Sticky_1["default"];
var Drawer_1 = __importDefault(__webpack_require__(/*! ./components/Drawer */ "./src/extra/js/components/Drawer.tsx"));
exports.Drawer = Drawer_1["default"];
var PopUp_1 = __importDefault(__webpack_require__(/*! ./components/PopUp */ "./src/extra/js/components/PopUp.tsx"));
exports.PopUp = PopUp_1["default"];
var TreeView_1 = __importDefault(__webpack_require__(/*! ./components/TreeView */ "./src/extra/js/components/TreeView.tsx"));
exports.TreeView = TreeView_1["default"];
var Toast_1 = __importDefault(__webpack_require__(/*! ./components/Toast */ "./src/extra/js/components/Toast.tsx"));
exports.Toast = Toast_1["default"];
var PageMap_1 = __importDefault(__webpack_require__(/*! ./components/PageMap */ "./src/extra/js/components/PageMap.tsx"));
exports.PageMap = PageMap_1["default"];


/***/ }),

/***/ "react":
/*!****************************************************************************************************!*\
  !*** external {"commonjs":"react","commonjs2":"react","amd":"react","umd":"react","root":"React"} ***!
  \****************************************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = __WEBPACK_EXTERNAL_MODULE_react__;

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ var __webpack_exports__ = (__webpack_exec__("./src/extra/js/index.ts"));
/******/ return __webpack_exports__;
/******/ }
]);
});
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGF6emxlcl9leHRyYV9lZGJiMDg4NjM2Y2QwNjIzMzQ5Yy5qcyIsIm1hcHBpbmdzIjoiQUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0QsTzs7Ozs7Ozs7QUNWQTs7Ozs7Ozs7Ozs7Ozs7OztBQ0FBLHlFQUEwQjtBQUMxQixtRkFBbUM7QUFHbkMsSUFBTSxLQUFLLEdBQUcsVUFBQyxFQUEwQjtRQUF6QixJQUFJLFlBQUUsTUFBTTtJQUN4QixRQUFRLElBQUksRUFBRTtRQUNWLEtBQUssS0FBSztZQUNOLE9BQU8sTUFBTSxDQUFDLENBQUMsQ0FBQyx3REFBb0IsQ0FBQyxDQUFDLENBQUMsd0RBQW9CLENBQUM7UUFDaEUsS0FBSyxPQUFPO1lBQ1IsT0FBTyxNQUFNLENBQUMsQ0FBQyxDQUFDLHdEQUFvQixDQUFDLENBQUMsQ0FBQyx3REFBb0IsQ0FBQztRQUNoRSxLQUFLLE1BQU07WUFDUCxPQUFPLE1BQU0sQ0FBQyxDQUFDLENBQUMsd0RBQW9CLENBQUMsQ0FBQyxDQUFDLHdEQUFvQixDQUFDO1FBQ2hFLEtBQUssUUFBUTtZQUNULE9BQU8sTUFBTSxDQUFDLENBQUMsQ0FBQyx3REFBb0IsQ0FBQyxDQUFDLENBQUMsd0RBQW9CLENBQUM7UUFDaEU7WUFDSSxPQUFPLElBQUksQ0FBQztLQUNuQjtBQUNMLENBQUMsQ0FBQztBQUVGOzs7Ozs7Ozs7Ozs7R0FZRztBQUNILElBQU0sTUFBTSxHQUFHLFVBQUMsS0FBa0I7SUFDdkIsY0FBVSxHQUNiLEtBQUssV0FEUSxFQUFFLFFBQVEsR0FDdkIsS0FBSyxTQURrQixFQUFFLEtBQUssR0FDOUIsS0FBSyxNQUR5QixFQUFFLFFBQVEsR0FDeEMsS0FBSyxTQURtQyxFQUFFLE1BQU0sR0FDaEQsS0FBSyxPQUQyQyxFQUFFLElBQUksR0FDdEQsS0FBSyxLQURpRCxFQUFFLGFBQWEsR0FDckUsS0FBSyxjQURnRSxDQUMvRDtJQUVWLElBQU0sR0FBRyxHQUFhLENBQUMsSUFB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LENBQ1QsQ0FBQztBQUNOLENBQUMsQ0FBQztBQUVGLFFBQVEsQ0FBQyxZQUFZLEdBQUc7SUFDcEIsbUJBQW1CLEVBQUUsR0FBRztJQUN4QixrQkFBa0IsRUFBRSxHQUFHO0lBQ3ZCLGNBQWMsRUFBRSxFQUFFO0NBQ3JCLENBQUM7QUFFRixrQkFBZSxRQUFRLENBQUM7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ3RLeEIsNkVBQTRCO0FBRTVCLHVIQUF5QztBQVdyQyxpQkFYRyxtQkFBTSxDQVdIO0FBVlYsb0hBQXVDO0FBV25DLGdCQVhHLGtCQUFLLENBV0g7QUFWVCwwSEFBMkM7QUFXdkMsa0JBWEcsb0JBQU8sQ0FXSDtBQVZYLHVIQUF5QztBQVdyQyxpQkFYRyxtQkFBTSxDQVdIO0FBVlYsdUhBQXlDO0FBV3JDLGlCQVhHLG1CQUFNLENBV0g7QUFWVixvSEFBdUM7QUFXbkMsZ0JBWEcsa0JBQUssQ0FXSDtBQVZULDZIQUE2QztBQVd6QyxtQkFYRyxxQkFBUSxDQVdIO0FBVlosb0hBQXVDO0FBV25DLGdCQVhHLGtCQUFLLENBV0g7QUFWVCwwSEFBMkM7QUFXdkMsa0JBWEcsb0JBQU8sQ0FXSDs7Ozs7Ozs7Ozs7O0FDckJYIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy93ZWJwYWNrL3VuaXZlcnNhbE1vZHVsZURlZmluaXRpb24/Iiwid2VicGFjazovLy8uL3NyYy9leHRyYS9zY3NzL2luZGV4LnNjc3MvLi9zcmMvZXh0cmEvc2Nzcy9pbmRleC5zY3NzPyIsIndlYnBhY2s6Ly8vLy4vc3JjL2V4dHJhL2pzL2NvbXBvbmVudHMvRHJhd2VyLnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL05vdGljZS50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvZXh0cmEvanMvY29tcG9uZW50cy9QYWdlTWFwLnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL1BhZ2VyLnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL1BvcFVwLnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL1NwaW5uZXIudHN4PyIsIndlYnBhY2s6Ly8vLy4vc3JjL2V4dHJhL2pzL2NvbXBvbmVudHMvU3RpY2t5LnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL1RvYXN0LnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9jb21wb25lbnRzL1RyZWVWaWV3LnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9leHRyYS9qcy9pbmRleC50cz8iLCJ3ZWJwYWNrOi8vLy9leHRlcm5hbCB7XCJjb21tb25qc1wiOlwicmVhY3RcIixcImNvbW1vbmpzMlwiOlwicmVhY3RcIixcImFtZFwiOlwicmVhY3RcIixcInVtZFwiOlwicmVhY3RcIixcInJvb3RcIjpcIlJlYWN0XCJ9PyJdLCJzb3VyY2VzQ29udGVudCI6WyIoZnVuY3Rpb24gd2VicGFja1VuaXZlcnNhbE1vZHVsZURlZmluaXRpb24ocm9vdCwgZmFjdG9yeSkge1xuXHRpZih0eXBlb2YgZXhwb3J0cyA9PT0gJ29iamVjdCcgJiYgdHlwZW9mIG1vZHVsZSA9PT0gJ29iamVjdCcpXG5cdFx0bW9kdWxlLmV4cG9ydHMgPSBmYWN0b3J5KHJlcXVpcmUoXCJyZWFjdFwiKSk7XG5cdGVsc2UgaWYodHlwZW9mIGRlZmluZSA9PT0gJ2Z1bmN0aW9uJyAmJiBkZWZpbmUuYW1kKVxuXHRcdGRlZmluZShbXCJyZWFjdFwiXSwgZmFjdG9yeSk7XG5cdGVsc2UgaWYodHlwZW9mIGV4cG9ydHMgPT09ICdvYmplY3QnKVxuXHRcdGV4cG9ydHNbXCJkYXp6bGVyX2V4dHJhXCJdID0gZmFjdG9yeShyZXF1aXJlKFwicmVhY3RcIikpO1xuXHRlbHNlXG5cdFx0cm9vdFtcImRhenpsZXJfZXh0cmFcIl0gPSBmYWN0b3J5KHJvb3RbXCJSZWFjdFwiXSk7XG59KShzZWxmLCBmdW5jdGlvbihfX1dFQlBBQ0tfRVhURVJOQUxfTU9EVUxFX3JlYWN0X18pIHtcbnJldHVybiAiLCIvLyBleHRyYWN0ZWQgYnkgbWluaS1jc3MtZXh0cmFjdC1wbHVnaW4iLCJpbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHtqb2luLCBjb25jYXR9IGZyb20gJ3JhbWRhJztcbmltcG9ydCB7Q2FyZXRQcm9wcywgRHJhd2VyUHJvcHN9IGZyb20gJy4uL3R5cGVzJztcblxuY29uc3QgQ2FyZXQgPSAoe3NpZGUsIG9wZW5lZH06IENhcmV0UHJvcHMpID0+IHtcbiAgICBzd2l0Y2ggKHNpZGUpIHtcbiAgICAgICAgY2FzZSAndG9wJzpcbiAgICAgICAgICAgIHJldHVybiBvcGVuZWQgPyA8c3Bhbj4mIzk2NTA7PC9zcGFuPiA6IDxzcGFuPiYjOTY2MDs8L3NwYW4+O1xuICAgICAgICBjYXNlICdyaWdodCc6XG4gICAgICAgICAgICByZXR1cm4gb3BlbmVkID8gPHNwYW4+JiM5NjU2Ozwvc3Bhbj4gOiA8c3Bhbj4mIzk2NjY7PC9zcGFuPjtcbiAgICAgICAgY2FzZSAnbGVmdCc6XG4gICAgICAgICAgICByZXR1cm4gb3BlbmVkID8gPHNwYW4+JiM5NjY2Ozwvc3Bhbj4gOiA8c3Bhbj4mIzk2NTY7PC9zcGFuPjtcbiAgICAgICAgY2FzZSAnYm90dG9tJzpcbiAgICAgICAgICAgIHJldHVybiBvcGVuZWQgPyA8c3Bhbj4mIzk2NjA7PC9zcGFuPiA6IDxzcGFuPiYjOTY1MDs8L3NwYW4+O1xuICAgICAgICBkZWZhdWx0OlxuICAgICAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxufTtcblxuLyoqXG4gKiBEcmF3IGNvbnRlbnQgZnJvbSB0aGUgc2lkZXMgb2YgdGhlIHNjcmVlbi5cbiAqXG4gKiA6Q1NTOlxuICpcbiAqICAgICAtIGBgZGF6emxlci1leHRyYS1kcmF3ZXJgYFxuICogICAgIC0gYGBkcmF3ZXItY29udGVudGBgXG4gKiAgICAgLSBgYGRyYXdlci1jb250cm9sYGBcbiAqICAgICAtIGBgdmVydGljYWxgYFxuICogICAgIC0gYGBob3Jpem9udGFsYGBcbiAqICAgICAtIGBgcmlnaHRgYFxuICogICAgIC0gYGBib3R0b21gYFxuICovXG5jb25zdCBEcmF3ZXIgPSAocHJvcHM6IERyYXdlclByb3BzKSA9PiB7XG4gICAgY29uc3Qge2NsYXNzX25hbWUsIGlkZW50aXR5LCBzdHlsZSwgY2hpbGRyZW4sIG9wZW5lZCwgc2lkZSwgdXBkYXRlQXNwZWN0c30gPVxuICAgICAgICBwcm9wcztcblxuICAgIGNvbnN0IGNzczogc3RyaW5nW10gPSBbc2lkZV07XG5cbiAgICBpZiAoc2lkZSA9PT0gJ3RvcCcgfHwgc2lkZSA9PT0gJ2JvdHRvbScpIHtcbiAgICAgICAgY3NzLnB1c2goJ2hvcml6b250YWwnKTtcbiAgICB9IGVsc2Uge1xuICAgICAgICBjc3MucHVzaCgndmVydGljYWwnKTtcbiAgICB9XG5cbiAgICByZXR1cm4gKFxuICAgICAgICA8ZGl2XG4gICAgICAgICAgICBjbGFzc05hbWU9e2pvaW4oJyAnLCBjb25jYXQoY3NzLCBbY2xhc3NfbmFtZV0pKX1cbiAgICAgICAgICAgIGlkPXtpZGVudGl0eX1cbiAgICAgICAgICAgIHN0eWxlPXtzdHlsZX1cbiAgICAgICAgPlxuICAgICAgICAgICAge29wZW5lZCAmJiAoXG4gICAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9e2pvaW4oJyAnLCBjb25jYXQoY3NzLCBbJ2RyYXdlci1jb250ZW50J10pKX0+XG4gICAgICAgICAgICAgICAgICAgIHtjaGlsZHJlbn1cbiAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICl9XG4gICAgICAgICAgICA8ZGl2XG4gICAgICAgICAgICAgICAgY2xhc3NOYW1lPXtqb2luKCcgJywgY29uY2F0KGNzcywgWydkcmF3ZXItY29udHJvbCddKSl9XG4gICAgICAgICAgICAgICAgb25DbGljaz17KCkgPT4gdXBkYXRlQXNwZWN0cyh7b3BlbmVkOiAhb3BlbmVkfSl9XG4gICAgICAgICAgICA+XG4gICAgICAgICAgICAgICAgPENhcmV0IG9wZW5lZD17b3BlbmVkfSBzaWRlPXtzaWRlfSAvPlxuICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgIDwvZGl2PlxuICAgICk7XG59O1xuXG5EcmF3ZXIuZGVmYXVsdFByb3BzID0ge1xuICAgIHNpZGU6ICd0b3AnLFxufTtcblxuZXhwb3J0IGRlZmF1bHQgRHJhd2VyO1xuIiwiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7dGltZXN0YW1wUHJvcH0gZnJvbSAnY29tbW9ucyc7XG5pbXBvcnQge21lcmdlfSBmcm9tICdyYW1kYSc7XG5pbXBvcnQge05vdGljZVByb3BzfSBmcm9tICcuLi90eXBlcyc7XG5cbi8qKlxuICogQnJvd3NlciBub3RpZmljYXRpb25zIHdpdGggcGVybWlzc2lvbnMgaGFuZGxpbmcuXG4gKi9cbmV4cG9ydCBkZWZhdWx0IGNsYXNzIE5vdGljZSBleHRlbmRzIFJlYWN0LkNvbXBvbmVudDxOb3RpY2VQcm9wcz4ge1xuICAgIGNvbnN0cnVjdG9yKHByb3BzKSB7XG4gICAgICAgIHN1cGVyKHByb3BzKTtcbiAgICAgICAgdGhpcy5zdGF0ZSA9IHtcbiAgICAgICAgICAgIGxhc3RNZXNzYWdlOiBwcm9wcy5ib2R5LFxuICAgICAgICAgICAgbm90aWZpY2F0aW9uOiBudWxsLFxuICAgICAgICB9O1xuICAgICAgICB0aGlzLm9uUGVybWlzc2lvbiA9IHRoaXMub25QZXJtaXNzaW9uLmJpbmQodGhpcyk7XG4gICAgfVxuXG4gICAgY29tcG9uZW50RGlkTW91bnQoKSB7XG4gICAgICAgIGNvbnN0IHt1cGRhdGVBc3BlY3RzfSA9IHRoaXMucHJvcHM7XG4gICAgICAgIGlmICghKCdOb3RpZmljYXRpb24nIGluIHdpbmRvdykgJiYgdXBkYXRlQXNwZWN0cykge1xuICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyh7cGVybWlzc2lvbjogJ3Vuc3VwcG9ydGVkJ30pO1xuICAgICAgICB9IGVsc2UgaWYgKE5vdGlmaWNhdGlvbi5wZXJtaXNzaW9uID09PSAnZGVmYXVsdCcpIHtcbiAgICAgICAgICAgIE5vdGlmaWNhdGlvbi5yZXF1ZXN0UGVybWlzc2lvbigpLnRoZW4odGhpcy5vblBlcm1pc3Npb24pO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgdGhpcy5vblBlcm1pc3Npb24od2luZG93Lk5vdGlmaWNhdGlvbi5wZXJtaXNzaW9uKTtcbiAgICAgICAgfVxuICAgIH1cblxuICAgIGNvbXBvbmVudERpZFVwZGF0ZShwcmV2UHJvcHMpIHtcbiAgICAgICAgaWYgKCFwcmV2UHJvcHMuZGlzcGxheWVkICYmIHRoaXMucHJvcHMuZGlzcGxheWVkKSB7XG4gICAgICAgICAgICB0aGlzLnNlbmROb3RpZmljYXRpb24odGhpcy5wcm9wcy5wZXJtaXNzaW9uKTtcbiAgICAgICAgfVxuICAgIH1cblxuICAgIHNlbmROb3RpZmljYXRpb24ocGVybWlzc2lvbikge1xuICAgICAgICBjb25zdCB7XG4gICAgICAgICAgICB1cGRhdGVBc3BlY3RzLFxuICAgICAgICAgICAgYm9keSxcbiAgICAgICAgICAgIHRpdGxlLFxuICAgICAgICAgICAgaWNvbixcbiAgICAgICAgICAgIHJlcXVpcmVfaW50ZXJhY3Rpb24sXG4gICAgICAgICAgICBsYW5nLFxuICAgICAgICAgICAgYmFkZ2UsXG4gICAgICAgICAgICB0YWcsXG4gICAgICAgICAgICBpbWFnZSxcbiAgICAgICAgICAgIHZpYnJhdGUsXG4gICAgICAgIH0gPSB0aGlzLnByb3BzO1xuICAgICAgICBpZiAocGVybWlzc2lvbiA9PT0gJ2dyYW50ZWQnKSB7XG4gICAgICAgICAgICBjb25zdCBvcHRpb25zID0ge1xuICAgICAgICAgICAgICAgIHJlcXVpcmVJbnRlcmFjdGlvbjogcmVxdWlyZV9pbnRlcmFjdGlvbixcbiAgICAgICAgICAgICAgICBib2R5LFxuICAgICAgICAgICAgICAgIGljb24sXG4gICAgICAgICAgICAgICAgbGFuZyxcbiAgICAgICAgICAgICAgICBiYWRnZSxcbiAgICAgICAgICAgICAgICB0YWcsXG4gICAgICAgICAgICAgICAgaW1hZ2UsXG4gICAgICAgICAgICAgICAgdmlicmF0ZSxcbiAgICAgICAgICAgIH07XG4gICAgICAgICAgICBjb25zdCBub3RpZmljYXRpb24gPSBuZXcgTm90aWZpY2F0aW9uKHRpdGxlLCBvcHRpb25zKTtcbiAgICAgICAgICAgIG5vdGlmaWNhdGlvbi5vbmNsaWNrID0gKCkgPT4ge1xuICAgICAgICAgICAgICAgIGlmICh1cGRhdGVBc3BlY3RzKSB7XG4gICAgICAgICAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMoXG4gICAgICAgICAgICAgICAgICAgICAgICBtZXJnZShcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB7ZGlzcGxheWVkOiBmYWxzZX0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdGltZXN0YW1wUHJvcCgnY2xpY2tzJywgdGhpcy5wcm9wcy5jbGlja3MgKyAxKVxuICAgICAgICAgICAgICAgICAgICAgICAgKVxuICAgICAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH07XG4gICAgICAgICAgICBub3RpZmljYXRpb24ub25jbG9zZSA9ICgpID0+IHtcbiAgICAgICAgICAgICAgICBpZiAodXBkYXRlQXNwZWN0cykge1xuICAgICAgICAgICAgICAgICAgICB1cGRhdGVBc3BlY3RzKFxuICAgICAgICAgICAgICAgICAgICAgICAgbWVyZ2UoXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAge2Rpc3BsYXllZDogZmFsc2V9LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpbWVzdGFtcFByb3AoJ2Nsb3NlcycsIHRoaXMucHJvcHMuY2xvc2VzICsgMSlcbiAgICAgICAgICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9O1xuICAgICAgICB9XG4gICAgfVxuXG4gICAgb25QZXJtaXNzaW9uKHBlcm1pc3Npb24pIHtcbiAgICAgICAgY29uc3Qge2Rpc3BsYXllZCwgdXBkYXRlQXNwZWN0c30gPSB0aGlzLnByb3BzO1xuICAgICAgICBpZiAodXBkYXRlQXNwZWN0cykge1xuICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyh7cGVybWlzc2lvbn0pO1xuICAgICAgICB9XG4gICAgICAgIGlmIChkaXNwbGF5ZWQpIHtcbiAgICAgICAgICAgIHRoaXMuc2VuZE5vdGlmaWNhdGlvbihwZXJtaXNzaW9uKTtcbiAgICAgICAgfVxuICAgIH1cblxuICAgIHJlbmRlcigpIHtcbiAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxuXG4gICAgc3RhdGljIGRlZmF1bHRQcm9wczoge1xuICAgICAgICByZXF1aXJlX2ludGVyYWN0aW9uOiBmYWxzZTtcbiAgICAgICAgY2xpY2tzOiAwO1xuICAgICAgICBjbGlja3NfdGltZXN0YW1wOiAtMTtcbiAgICAgICAgY2xvc2VzOiAwO1xuICAgICAgICBjbG9zZXNfdGltZXN0YW1wOiAtMTtcbiAgICB9O1xufVxuIiwiaW1wb3J0IFJlYWN0LCB7dXNlRWZmZWN0LCB1c2VTdGF0ZX0gZnJvbSAncmVhY3QnO1xuaW1wb3J0IHtEYXp6bGVyUHJvcHN9IGZyb20gJy4uLy4uLy4uL2NvbW1vbnMvanMvdHlwZXMnO1xuXG4vKipcbiAqIExpc3Qgb2YgbGlua3MgdG8gb3RoZXIgcGFnZSBpbiB0aGUgYXBwLlxuICpcbiAqIDpDU1M6XG4gKlxuICogICAgIC0gYGBkYXp6bGVyLWV4dHJhLXBhZ2UtbWFwYGBcbiAqL1xuY29uc3QgUGFnZU1hcCA9IChwcm9wczogRGF6emxlclByb3BzKSA9PiB7XG4gICAgY29uc3Qge2NsYXNzX25hbWUsIHN0eWxlLCBpZGVudGl0eX0gPSBwcm9wcztcbiAgICBjb25zdCBbcGFnZU1hcCwgc2V0UGFnZU1hcF0gPSB1c2VTdGF0ZShudWxsKTtcblxuICAgIHVzZUVmZmVjdCgoKSA9PiB7XG4gICAgICAgIC8vIEB0cy1pZ25vcmVcbiAgICAgICAgZmV0Y2goYCR7d2luZG93LmRhenpsZXJfYmFzZV91cmx9L2RhenpsZXIvcGFnZS1tYXBgKS50aGVuKChyZXApID0+XG4gICAgICAgICAgICByZXAuanNvbigpLnRoZW4oc2V0UGFnZU1hcClcbiAgICAgICAgKTtcbiAgICB9LCBbXSk7XG5cbiAgICByZXR1cm4gKFxuICAgICAgICA8dWwgY2xhc3NOYW1lPXtjbGFzc19uYW1lfSBzdHlsZT17c3R5bGV9IGlkPXtpZGVudGl0eX0+XG4gICAgICAgICAgICB7cGFnZU1hcCAmJlxuICAgICAgICAgICAgICAgIHBhZ2VNYXAubWFwKChwYWdlKSA9PiAoXG4gICAgICAgICAgICAgICAgICAgIDxsaSBrZXk9e3BhZ2UubmFtZX0+XG4gICAgICAgICAgICAgICAgICAgICAgICA8YSBocmVmPXtwYWdlLnVybH0+e3BhZ2UudGl0bGV9PC9hPlxuICAgICAgICAgICAgICAgICAgICA8L2xpPlxuICAgICAgICAgICAgICAgICkpfVxuICAgICAgICA8L3VsPlxuICAgICk7XG59O1xuXG5QYWdlTWFwLmRlZmF1bHRQcm9wcyA9IHt9O1xuXG5leHBvcnQgZGVmYXVsdCBQYWdlTWFwO1xuIiwiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7cmFuZ2UsIGpvaW59IGZyb20gJ3JhbWRhJztcbmltcG9ydCB7UGFnZXJQYWdlUHJvcHMsIFBhZ2VyUHJvcHMsIFBhZ2VyU3RhdGV9IGZyb20gJy4uL3R5cGVzJztcblxuY29uc3Qgc3RhcnRPZmZzZXQgPSAocGFnZSwgaXRlbVBlclBhZ2UpID0+XG4gICAgKHBhZ2UgLSAxKSAqIChwYWdlID4gMSA/IGl0ZW1QZXJQYWdlIDogMCk7XG5cbmNvbnN0IGVuZE9mZnNldCA9IChzdGFydCwgaXRlbVBlclBhZ2UsIHBhZ2UsIHRvdGFsLCBsZWZ0T3ZlcikgPT5cbiAgICBwYWdlICE9PSB0b3RhbFxuICAgICAgICA/IHN0YXJ0ICsgaXRlbVBlclBhZ2VcbiAgICAgICAgOiBsZWZ0T3ZlciAhPT0gMFxuICAgICAgICA/IHN0YXJ0ICsgbGVmdE92ZXJcbiAgICAgICAgOiBzdGFydCArIGl0ZW1QZXJQYWdlO1xuXG5jb25zdCBzaG93TGlzdCA9IChwYWdlLCB0b3RhbCwgbikgPT4ge1xuICAgIGlmICh0b3RhbCA+IG4pIHtcbiAgICAgICAgY29uc3QgbWlkZGxlID0gbiAvIDI7XG4gICAgICAgIGNvbnN0IGZpcnN0ID1cbiAgICAgICAgICAgIHBhZ2UgPj0gdG90YWwgLSBtaWRkbGVcbiAgICAgICAgICAgICAgICA/IHRvdGFsIC0gbiArIDFcbiAgICAgICAgICAgICAgICA6IHBhZ2UgPiBtaWRkbGVcbiAgICAgICAgICAgICAgICA/IHBhZ2UgLSBtaWRkbGVcbiAgICAgICAgICAgICAgICA6IDE7XG4gICAgICAgIGNvbnN0IGxhc3QgPSBwYWdlIDwgdG90YWwgLSBtaWRkbGUgPyBmaXJzdCArIG4gOiB0b3RhbCArIDE7XG4gICAgICAgIHJldHVybiByYW5nZShmaXJzdCwgbGFzdCk7XG4gICAgfVxuICAgIHJldHVybiByYW5nZSgxLCB0b3RhbCArIDEpO1xufTtcblxuY29uc3QgUGFnZSA9ICh7c3R5bGUsIGNsYXNzX25hbWUsIG9uX2NoYW5nZSwgdGV4dCwgcGFnZX06IFBhZ2VyUGFnZVByb3BzKSA9PiAoXG4gICAgPHNwYW4gc3R5bGU9e3N0eWxlfSBjbGFzc05hbWU9e2NsYXNzX25hbWV9IG9uQ2xpY2s9eygpID0+IG9uX2NoYW5nZShwYWdlKX0+XG4gICAgICAgIHt0ZXh0IHx8IHBhZ2V9XG4gICAgPC9zcGFuPlxuKTtcblxuLyoqXG4gKiBQYWdpbmcgZm9yIGRhenpsZXIgYXBwcy5cbiAqXG4gKiA6Q1NTOlxuICpcbiAqICAgICAtIGBgZGF6emxlci1leHRyYS1wYWdlcmBgXG4gKiAgICAgLSBgYHBhZ2VgYFxuICovXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBQYWdlciBleHRlbmRzIFJlYWN0LkNvbXBvbmVudDxQYWdlclByb3BzLCBQYWdlclN0YXRlPiB7XG4gICAgY29uc3RydWN0b3IocHJvcHMpIHtcbiAgICAgICAgc3VwZXIocHJvcHMpO1xuICAgICAgICB0aGlzLnN0YXRlID0ge1xuICAgICAgICAgICAgY3VycmVudF9wYWdlOiBudWxsLFxuICAgICAgICAgICAgc3RhcnRfb2Zmc2V0OiBudWxsLFxuICAgICAgICAgICAgZW5kX29mZnNldDogbnVsbCxcbiAgICAgICAgICAgIHBhZ2VzOiBbXSxcbiAgICAgICAgICAgIHRvdGFsX3BhZ2VzOiBNYXRoLmNlaWwocHJvcHMudG90YWxfaXRlbXMgLyBwcm9wcy5pdGVtc19wZXJfcGFnZSksXG4gICAgICAgIH07XG4gICAgICAgIHRoaXMub25DaGFuZ2VQYWdlID0gdGhpcy5vbkNoYW5nZVBhZ2UuYmluZCh0aGlzKTtcbiAgICB9XG5cbiAgICBVTlNBRkVfY29tcG9uZW50V2lsbE1vdW50KCkge1xuICAgICAgICB0aGlzLm9uQ2hhbmdlUGFnZSh0aGlzLnByb3BzLmN1cnJlbnRfcGFnZSk7XG4gICAgfVxuXG4gICAgb25DaGFuZ2VQYWdlKHBhZ2UpIHtcbiAgICAgICAgY29uc3Qge2l0ZW1zX3Blcl9wYWdlLCB0b3RhbF9pdGVtcywgdXBkYXRlQXNwZWN0cywgcGFnZXNfZGlzcGxheWVkfSA9XG4gICAgICAgICAgICB0aGlzLnByb3BzO1xuICAgICAgICBjb25zdCB7dG90YWxfcGFnZXN9ID0gdGhpcy5zdGF0ZTtcblxuICAgICAgICBjb25zdCBzdGFydF9vZmZzZXQgPSBzdGFydE9mZnNldChwYWdlLCBpdGVtc19wZXJfcGFnZSk7XG4gICAgICAgIGNvbnN0IGxlZnRPdmVyID0gdG90YWxfaXRlbXMgJSBpdGVtc19wZXJfcGFnZTtcblxuICAgICAgICBjb25zdCBlbmRfb2Zmc2V0ID0gZW5kT2Zmc2V0KFxuICAgICAgICAgICAgc3RhcnRfb2Zmc2V0LFxuICAgICAgICAgICAgaXRlbXNfcGVyX3BhZ2UsXG4gICAgICAgICAgICBwYWdlLFxuICAgICAgICAgICAgdG90YWxfcGFnZXMsXG4gICAgICAgICAgICBsZWZ0T3ZlclxuICAgICAgICApO1xuXG4gICAgICAgIGNvbnN0IHBheWxvYWQ6IFBhZ2VyU3RhdGUgPSB7XG4gICAgICAgICAgICBjdXJyZW50X3BhZ2U6IHBhZ2UsXG4gICAgICAgICAgICBzdGFydF9vZmZzZXQ6IHN0YXJ0X29mZnNldCxcbiAgICAgICAgICAgIGVuZF9vZmZzZXQ6IGVuZF9vZmZzZXQsXG4gICAgICAgICAgICBwYWdlczogc2hvd0xpc3QocGFnZSwgdG90YWxfcGFnZXMsIHBhZ2VzX2Rpc3BsYXllZCksXG4gICAgICAgIH07XG4gICAgICAgIHRoaXMuc2V0U3RhdGUocGF5bG9hZCk7XG5cbiAgICAgICAgaWYgKHVwZGF0ZUFzcGVjdHMpIHtcbiAgICAgICAgICAgIGlmICh0aGlzLnN0YXRlLnRvdGFsX3BhZ2VzICE9PSB0aGlzLnByb3BzLnRvdGFsX3BhZ2VzKSB7XG4gICAgICAgICAgICAgICAgcGF5bG9hZC50b3RhbF9wYWdlcyA9IHRoaXMuc3RhdGUudG90YWxfcGFnZXM7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICB1cGRhdGVBc3BlY3RzKHBheWxvYWQpO1xuICAgICAgICB9XG4gICAgfVxuXG4gICAgVU5TQUZFX2NvbXBvbmVudFdpbGxSZWNlaXZlUHJvcHMocHJvcHMpIHtcbiAgICAgICAgaWYgKHByb3BzLmN1cnJlbnRfcGFnZSAhPT0gdGhpcy5zdGF0ZS5jdXJyZW50X3BhZ2UpIHtcbiAgICAgICAgICAgIHRoaXMub25DaGFuZ2VQYWdlKHByb3BzLmN1cnJlbnRfcGFnZSk7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICByZW5kZXIoKSB7XG4gICAgICAgIGNvbnN0IHtjdXJyZW50X3BhZ2UsIHBhZ2VzLCB0b3RhbF9wYWdlc30gPSB0aGlzLnN0YXRlO1xuICAgICAgICBjb25zdCB7Y2xhc3NfbmFtZSwgaWRlbnRpdHksIHBhZ2Vfc3R5bGUsIHBhZ2VfY2xhc3NfbmFtZX0gPSB0aGlzLnByb3BzO1xuXG4gICAgICAgIGNvbnN0IGNzczogc3RyaW5nW10gPSBbJ3BhZ2UnXTtcbiAgICAgICAgaWYgKHBhZ2VfY2xhc3NfbmFtZSkge1xuICAgICAgICAgICAgY3NzLnB1c2gocGFnZV9jbGFzc19uYW1lKTtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCBwYWdlQ3NzID0gam9pbignICcsIGNzcyk7XG5cbiAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPXtjbGFzc19uYW1lfSBpZD17aWRlbnRpdHl9PlxuICAgICAgICAgICAgICAgIHtjdXJyZW50X3BhZ2UgPiAxICYmIChcbiAgICAgICAgICAgICAgICAgICAgPFBhZ2VcbiAgICAgICAgICAgICAgICAgICAgICAgIHBhZ2U9ezF9XG4gICAgICAgICAgICAgICAgICAgICAgICB0ZXh0PXsnZmlyc3QnfVxuICAgICAgICAgICAgICAgICAgICAgICAgc3R5bGU9e3BhZ2Vfc3R5bGV9XG4gICAgICAgICAgICAgICAgICAgICAgICBjbGFzc19uYW1lPXtwYWdlQ3NzfVxuICAgICAgICAgICAgICAgICAgICAgICAgb25fY2hhbmdlPXt0aGlzLm9uQ2hhbmdlUGFnZX1cbiAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICApfVxuICAgICAgICAgICAgICAgIHtjdXJyZW50X3BhZ2UgPiAxICYmIChcbiAgICAgICAgICAgICAgICAgICAgPFBhZ2VcbiAgICAgICAgICAgICAgICAgICAgICAgIHBhZ2U9e2N1cnJlbnRfcGFnZSAtIDF9XG4gICAgICAgICAgICAgICAgICAgICAgICB0ZXh0PXsncHJldmlvdXMnfVxuICAgICAgICAgICAgICAgICAgICAgICAgc3R5bGU9e3BhZ2Vfc3R5bGV9XG4gICAgICAgICAgICAgICAgICAgICAgICBjbGFzc19uYW1lPXtwYWdlQ3NzfVxuICAgICAgICAgICAgICAgICAgICAgICAgb25fY2hhbmdlPXt0aGlzLm9uQ2hhbmdlUGFnZX1cbiAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICApfVxuICAgICAgICAgICAgICAgIHtwYWdlcy5tYXAoKGUpID0+IChcbiAgICAgICAgICAgICAgICAgICAgPFBhZ2VcbiAgICAgICAgICAgICAgICAgICAgICAgIHBhZ2U9e2V9XG4gICAgICAgICAgICAgICAgICAgICAgICBrZXk9e2BwYWdlLSR7ZX1gfVxuICAgICAgICAgICAgICAgICAgICAgICAgc3R5bGU9e3BhZ2Vfc3R5bGV9XG4gICAgICAgICAgICAgICAgICAgICAgICBjbGFzc19uYW1lPXtwYWdlQ3NzfVxuICAgICAgICAgICAgICAgICAgICAgICAgb25fY2hhbmdlPXt0aGlzLm9uQ2hhbmdlUGFnZX1cbiAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICApKX1cbiAgICAgICAgICAgICAgICB7Y3VycmVudF9wYWdlIDwgdG90YWxfcGFnZXMgJiYgKFxuICAgICAgICAgICAgICAgICAgICA8UGFnZVxuICAgICAgICAgICAgICAgICAgICAgICAgcGFnZT17Y3VycmVudF9wYWdlICsgMX1cbiAgICAgICAgICAgICAgICAgICAgICAgIHRleHQ9eyduZXh0J31cbiAgICAgICAgICAgICAgICAgICAgICAgIHN0eWxlPXtwYWdlX3N0eWxlfVxuICAgICAgICAgICAgICAgICAgICAgICAgY2xhc3NfbmFtZT17cGFnZUNzc31cbiAgICAgICAgICAgICAgICAgICAgICAgIG9uX2NoYW5nZT17dGhpcy5vbkNoYW5nZVBhZ2V9XG4gICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgKX1cbiAgICAgICAgICAgICAgICB7Y3VycmVudF9wYWdlIDwgdG90YWxfcGFnZXMgJiYgKFxuICAgICAgICAgICAgICAgICAgICA8UGFnZVxuICAgICAgICAgICAgICAgICAgICAgICAgcGFnZT17dG90YWxfcGFnZXN9XG4gICAgICAgICAgICAgICAgICAgICAgICB0ZXh0PXsnbGFzdCd9XG4gICAgICAgICAgICAgICAgICAgICAgICBzdHlsZT17cGFnZV9zdHlsZX1cbiAgICAgICAgICAgICAgICAgICAgICAgIGNsYXNzX25hbWU9e3BhZ2VDc3N9XG4gICAgICAgICAgICAgICAgICAgICAgICBvbl9jaGFuZ2U9e3RoaXMub25DaGFuZ2VQYWdlfVxuICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICl9XG4gICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgKTtcbiAgICB9XG4gICAgc3RhdGljIGRlZmF1bHRQcm9wcyA9IHtcbiAgICAgICAgY3VycmVudF9wYWdlOiAxLFxuICAgICAgICBpdGVtc19wZXJfcGFnZTogMTAsXG4gICAgICAgIHBhZ2VzX2Rpc3BsYXllZDogMTAsXG4gICAgfTtcbn1cbiIsImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQge1BvcFVwUHJvcHN9IGZyb20gJy4uL3R5cGVzJztcblxuZnVuY3Rpb24gZ2V0TW91c2VYKGUsIHBvcHVwKSB7XG4gICAgcmV0dXJuIChcbiAgICAgICAgZS5jbGllbnRYIC1cbiAgICAgICAgZS50YXJnZXQuZ2V0Qm91bmRpbmdDbGllbnRSZWN0KCkubGVmdCAtXG4gICAgICAgIHBvcHVwLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLndpZHRoIC8gMlxuICAgICk7XG59XG5cbnR5cGUgUG9wVXBTdGF0ZSA9IHtcbiAgICBwb3M/OiBudW1iZXI7XG59O1xuXG4vKipcbiAqIFdyYXBzIGEgY29tcG9uZW50L3RleHQgdG8gcmVuZGVyIGEgcG9wdXAgd2hlbiBob3ZlcmluZ1xuICogb3ZlciB0aGUgY2hpbGRyZW4gb3IgY2xpY2tpbmcgb24gaXQuXG4gKlxuICogOkNTUzpcbiAqXG4gKiAgICAgLSBgYGRhenpsZXItZXh0cmEtcG9wLXVwYGBcbiAqICAgICAtIGBgcG9wdXAtY29udGVudGBgXG4gKiAgICAgLSBgYHZpc2libGVgYFxuICovXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBQb3BVcCBleHRlbmRzIFJlYWN0LkNvbXBvbmVudDxQb3BVcFByb3BzLCBQb3BVcFN0YXRlPiB7XG4gICAgcG9wdXBSZWY/OiBhbnk7XG5cbiAgICBjb25zdHJ1Y3Rvcihwcm9wcykge1xuICAgICAgICBzdXBlcihwcm9wcyk7XG4gICAgICAgIHRoaXMuc3RhdGUgPSB7XG4gICAgICAgICAgICBwb3M6IG51bGwsXG4gICAgICAgIH07XG4gICAgfVxuICAgIHJlbmRlcigpIHtcbiAgICAgICAgY29uc3Qge1xuICAgICAgICAgICAgY2xhc3NfbmFtZSxcbiAgICAgICAgICAgIHN0eWxlLFxuICAgICAgICAgICAgaWRlbnRpdHksXG4gICAgICAgICAgICBjaGlsZHJlbixcbiAgICAgICAgICAgIGNvbnRlbnQsXG4gICAgICAgICAgICBtb2RlLFxuICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyxcbiAgICAgICAgICAgIGFjdGl2ZSxcbiAgICAgICAgICAgIGNvbnRlbnRfc3R5bGUsXG4gICAgICAgICAgICBjaGlsZHJlbl9zdHlsZSxcbiAgICAgICAgfSA9IHRoaXMucHJvcHM7XG5cbiAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPXtjbGFzc19uYW1lfSBzdHlsZT17c3R5bGV9IGlkPXtpZGVudGl0eX0+XG4gICAgICAgICAgICAgICAgPGRpdlxuICAgICAgICAgICAgICAgICAgICBjbGFzc05hbWU9eydwb3B1cC1jb250ZW50JyArIChhY3RpdmUgPyAnIHZpc2libGUnIDogJycpfVxuICAgICAgICAgICAgICAgICAgICBzdHlsZT17e1xuICAgICAgICAgICAgICAgICAgICAgICAgLi4uKGNvbnRlbnRfc3R5bGUgfHwge30pLFxuICAgICAgICAgICAgICAgICAgICAgICAgbGVmdDogdGhpcy5zdGF0ZS5wb3MgfHwgMCxcbiAgICAgICAgICAgICAgICAgICAgfX1cbiAgICAgICAgICAgICAgICAgICAgcmVmPXsocikgPT4gKHRoaXMucG9wdXBSZWYgPSByKX1cbiAgICAgICAgICAgICAgICA+XG4gICAgICAgICAgICAgICAgICAgIHtjb250ZW50fVxuICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgICAgIDxkaXZcbiAgICAgICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwicG9wdXAtY2hpbGRyZW5cIlxuICAgICAgICAgICAgICAgICAgICBvbk1vdXNlRW50ZXI9eyhlKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgICAgICBpZiAobW9kZSA9PT0gJ2hvdmVyJykge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRoaXMuc2V0U3RhdGUoXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHtwb3M6IGdldE1vdXNlWChlLCB0aGlzLnBvcHVwUmVmKX0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICgpID0+IHVwZGF0ZUFzcGVjdHMoe2FjdGl2ZTogdHJ1ZX0pXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgfX1cbiAgICAgICAgICAgICAgICAgICAgb25Nb3VzZUxlYXZlPXsoKSA9PlxuICAgICAgICAgICAgICAgICAgICAgICAgbW9kZSA9PT0gJ2hvdmVyJyAmJiB1cGRhdGVBc3BlY3RzKHthY3RpdmU6IGZhbHNlfSlcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICBvbkNsaWNrPXsoZSkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKG1vZGUgPT09ICdjbGljaycpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aGlzLnNldFN0YXRlKFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7cG9zOiBnZXRNb3VzZVgoZSwgdGhpcy5wb3B1cFJlZil9LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAoKSA9PiB1cGRhdGVBc3BlY3RzKHthY3RpdmU6ICFhY3RpdmV9KVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIH19XG4gICAgICAgICAgICAgICAgICAgIHN0eWxlPXtjaGlsZHJlbl9zdHlsZX1cbiAgICAgICAgICAgICAgICA+XG4gICAgICAgICAgICAgICAgICAgIHtjaGlsZHJlbn1cbiAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICApO1xuICAgIH1cblxuICAgIHN0YXRpYyBkZWZhdWx0UHJvcHMgPSB7XG4gICAgICAgIG1vZGU6ICdob3ZlcicsXG4gICAgICAgIGFjdGl2ZTogZmFsc2UsXG4gICAgfTtcbn1cbiIsImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQge0RhenpsZXJQcm9wc30gZnJvbSAnLi4vLi4vLi4vY29tbW9ucy9qcy90eXBlcyc7XG5cbi8qKlxuICogU2ltcGxlIGh0bWwvY3NzIHNwaW5uZXIuXG4gKi9cbmNvbnN0IFNwaW5uZXIgPSAocHJvcHM6IERhenpsZXJQcm9wcykgPT4ge1xuICAgIGNvbnN0IHtjbGFzc19uYW1lLCBzdHlsZSwgaWRlbnRpdHl9ID0gcHJvcHM7XG4gICAgcmV0dXJuIDxkaXYgaWQ9e2lkZW50aXR5fSBjbGFzc05hbWU9e2NsYXNzX25hbWV9IHN0eWxlPXtzdHlsZX0gLz47XG59O1xuXG5leHBvcnQgZGVmYXVsdCBTcGlubmVyO1xuIiwiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7bWVyZ2VBbGx9IGZyb20gJ3JhbWRhJztcbmltcG9ydCB7U3RpY2t5UHJvcHN9IGZyb20gJy4uL3R5cGVzJztcblxuLyoqXG4gKiBBIHNob3J0aGFuZCBjb21wb25lbnQgZm9yIGEgc3RpY2t5IGRpdi5cbiAqL1xuY29uc3QgU3RpY2t5ID0gKHByb3BzOiBTdGlja3lQcm9wcykgPT4ge1xuICAgIGNvbnN0IHtjbGFzc19uYW1lLCBpZGVudGl0eSwgc3R5bGUsIGNoaWxkcmVuLCB0b3AsIGxlZnQsIHJpZ2h0LCBib3R0b219ID1cbiAgICAgICAgcHJvcHM7XG4gICAgY29uc3Qgc3R5bGVzID0gbWVyZ2VBbGwoW3N0eWxlLCB7dG9wLCBsZWZ0LCByaWdodCwgYm90dG9tfV0pO1xuICAgIHJldHVybiAoXG4gICAgICAgIDxkaXYgY2xhc3NOYW1lPXtjbGFzc19uYW1lfSBpZD17aWRlbnRpdHl9IHN0eWxlPXtzdHlsZXN9PlxuICAgICAgICAgICAge2NoaWxkcmVufVxuICAgICAgICA8L2Rpdj5cbiAgICApO1xufTtcblxuZXhwb3J0IGRlZmF1bHQgU3RpY2t5O1xuIiwiaW1wb3J0IFJlYWN0LCB7dXNlRWZmZWN0LCB1c2VNZW1vLCB1c2VTdGF0ZX0gZnJvbSAncmVhY3QnO1xuaW1wb3J0IHtqb2lufSBmcm9tICdyYW1kYSc7XG5pbXBvcnQge1RvYXN0UHJvcHN9IGZyb20gJy4uL3R5cGVzJztcblxuLyoqXG4gKiBEaXNwbGF5IGEgbWVzc2FnZSBvdmVyIHRoZSB1aSB0aGF0IHdpbGwgZGlzYXBwZWFycyBhZnRlciBhIGRlbGF5LlxuICpcbiAqIDpDU1M6XG4gKlxuICogICAgIC0gYGBkYXp6bGVyLWV4dHJhLXRvYXN0YGBcbiAqICAgICAtIGBgb3BlbmVkYGBcbiAqICAgICAtIGBgdG9hc3QtaW5uZXJgYFxuICogICAgIC0gYGB0b3BgYFxuICogICAgIC0gYGB0b3AtbGVmdGBgXG4gKiAgICAgLSBgYHRvcC1yaWdodGBgXG4gKiAgICAgLSBgYGJvdHRvbWBgXG4gKiAgICAgLSBgYGJvdHRvbS1sZWZ0YGBcbiAqICAgICAtIGBgYm90dG9tLXJpZ2h0YGBcbiAqICAgICAtIGBgcmlnaHRgYFxuICovXG5jb25zdCBUb2FzdCA9IChwcm9wczogVG9hc3RQcm9wcykgPT4ge1xuICAgIGNvbnN0IHtcbiAgICAgICAgY2xhc3NfbmFtZSxcbiAgICAgICAgc3R5bGUsXG4gICAgICAgIGlkZW50aXR5LFxuICAgICAgICBtZXNzYWdlLFxuICAgICAgICBwb3NpdGlvbixcbiAgICAgICAgb3BlbmVkLFxuICAgICAgICBkZWxheSxcbiAgICAgICAgdXBkYXRlQXNwZWN0cyxcbiAgICB9ID0gcHJvcHM7XG4gICAgY29uc3QgW2Rpc3BsYXllZCwgc2V0RGlzcGxheWVkXSA9IHVzZVN0YXRlKGZhbHNlKTtcblxuICAgIGNvbnN0IGNzcyA9IHVzZU1lbW8oKCkgPT4ge1xuICAgICAgICBjb25zdCBjID0gW2NsYXNzX25hbWUsIHBvc2l0aW9uXTtcbiAgICAgICAgaWYgKG9wZW5lZCkge1xuICAgICAgICAgICAgYy5wdXNoKCdvcGVuZWQnKTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gam9pbignICcsIGMpO1xuICAgIH0sIFtjbGFzc19uYW1lLCBvcGVuZWQsIHBvc2l0aW9uXSk7XG4gICAgdXNlRWZmZWN0KCgpID0+IHtcbiAgICAgICAgaWYgKG9wZW5lZCAmJiAhZGlzcGxheWVkKSB7XG4gICAgICAgICAgICBzZXRUaW1lb3V0KCgpID0+IHtcbiAgICAgICAgICAgICAgICB1cGRhdGVBc3BlY3RzKHtvcGVuZWQ6IGZhbHNlfSk7XG4gICAgICAgICAgICAgICAgc2V0RGlzcGxheWVkKGZhbHNlKTtcbiAgICAgICAgICAgIH0sIGRlbGF5KTtcbiAgICAgICAgICAgIHNldERpc3BsYXllZCh0cnVlKTtcbiAgICAgICAgfVxuICAgIH0sIFtvcGVuZWQsIGRpc3BsYXllZCwgZGVsYXldKTtcblxuICAgIHJldHVybiAoXG4gICAgICAgIDxkaXYgY2xhc3NOYW1lPXtjc3N9IHN0eWxlPXtzdHlsZX0gaWQ9e2lkZW50aXR5fT5cbiAgICAgICAgICAgIHttZXNzYWdlfVxuICAgICAgICA8L2Rpdj5cbiAgICApO1xufTtcblxuVG9hc3QuZGVmYXVsdFByb3BzID0ge1xuICAgIGRlbGF5OiAzMDAwLFxuICAgIHBvc2l0aW9uOiAndG9wJyxcbiAgICBvcGVuZWQ6IHRydWUsXG59O1xuXG5leHBvcnQgZGVmYXVsdCBUb2FzdDtcbiIsImltcG9ydCBSZWFjdCwge3VzZU1lbW99IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7aXMsIGpvaW4sIGluY2x1ZGVzLCBzcGxpdCwgc2xpY2UsIGNvbmNhdCwgd2l0aG91dH0gZnJvbSAncmFtZGEnO1xuaW1wb3J0IHtUcmVlVmlld0l0ZW1Qcm9wcywgVHJlZVZpZXdQcm9wc30gZnJvbSAnLi4vdHlwZXMnO1xuXG5jb25zdCBUcmVlVmlld0VsZW1lbnQgPSAoe1xuICAgIGxhYmVsLFxuICAgIG9uQ2xpY2ssXG4gICAgaWRlbnRpZmllcixcbiAgICBpdGVtcyxcbiAgICBsZXZlbCxcbiAgICBzZWxlY3RlZCxcbiAgICBleHBhbmRlZF9pdGVtcyxcbiAgICBuZXN0X2ljb25fZXhwYW5kZWQsXG4gICAgbmVzdF9pY29uX2NvbGxhcHNlZCxcbn06IFRyZWVWaWV3SXRlbVByb3BzKSA9PiB7XG4gICAgY29uc3QgaXNTZWxlY3RlZCA9IHVzZU1lbW8oXG4gICAgICAgICgpID0+IHNlbGVjdGVkICYmIGluY2x1ZGVzKGlkZW50aWZpZXIsIHNlbGVjdGVkKSxcbiAgICAgICAgW3NlbGVjdGVkLCBpZGVudGlmaWVyXVxuICAgICk7XG4gICAgY29uc3QgaXNFeHBhbmRlZCA9IHVzZU1lbW8oXG4gICAgICAgICgpID0+IGluY2x1ZGVzKGlkZW50aWZpZXIsIGV4cGFuZGVkX2l0ZW1zKSxcbiAgICAgICAgW2V4cGFuZGVkX2l0ZW1zLCBleHBhbmRlZF9pdGVtc11cbiAgICApO1xuICAgIGNvbnN0IGNzcyA9IFsndHJlZS1pdGVtLWxhYmVsJywgYGxldmVsLSR7bGV2ZWx9YF07XG4gICAgaWYgKGlzU2VsZWN0ZWQpIHtcbiAgICAgICAgY3NzLnB1c2goJ3NlbGVjdGVkJyk7XG4gICAgfVxuXG4gICAgcmV0dXJuIChcbiAgICAgICAgPGRpdlxuICAgICAgICAgICAgY2xhc3NOYW1lPXtgdHJlZS1pdGVtIGxldmVsLSR7bGV2ZWx9YH1cbiAgICAgICAgICAgIHN0eWxlPXt7bWFyZ2luTGVmdDogYCR7bGV2ZWx9cmVtYH19XG4gICAgICAgID5cbiAgICAgICAgICAgIDxkaXZcbiAgICAgICAgICAgICAgICBjbGFzc05hbWU9e2pvaW4oJyAnLCBjc3MpfVxuICAgICAgICAgICAgICAgIG9uQ2xpY2s9eyhlKSA9PiBvbkNsaWNrKGUsIGlkZW50aWZpZXIsIEJvb2xlYW4oaXRlbXMpKX1cbiAgICAgICAgICAgID5cbiAgICAgICAgICAgICAgICB7aXRlbXMgJiYgKFxuICAgICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzc05hbWU9XCJ0cmVlLWNhcmV0XCI+XG4gICAgICAgICAgICAgICAgICAgICAgICB7aXNFeHBhbmRlZCA/IG5lc3RfaWNvbl9leHBhbmRlZCA6IG5lc3RfaWNvbl9jb2xsYXBzZWR9XG4gICAgICAgICAgICAgICAgICAgIDwvc3Bhbj5cbiAgICAgICAgICAgICAgICApfVxuICAgICAgICAgICAgICAgIHtsYWJlbCB8fCBpZGVudGlmaWVyfVxuICAgICAgICAgICAgPC9kaXY+XG5cbiAgICAgICAgICAgIHtpdGVtcyAmJiBpc0V4cGFuZGVkICYmIChcbiAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cInRyZWUtc3ViLWl0ZW1zXCI+XG4gICAgICAgICAgICAgICAgICAgIHtpdGVtcy5tYXAoKGl0ZW0pID0+XG4gICAgICAgICAgICAgICAgICAgICAgICByZW5kZXJJdGVtKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXJlbnQ6IGlkZW50aWZpZXIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgb25DbGljayxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpdGVtLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxldmVsOiBsZXZlbCArIDEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgc2VsZWN0ZWQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbmVzdF9pY29uX2V4cGFuZGVkLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5lc3RfaWNvbl9jb2xsYXBzZWQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgZXhwYW5kZWRfaXRlbXMsXG4gICAgICAgICAgICAgICAgICAgICAgICB9KVxuICAgICAgICAgICAgICAgICAgICApfVxuICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgKX1cbiAgICAgICAgPC9kaXY+XG4gICAgKTtcbn07XG5cbmNvbnN0IHJlbmRlckl0ZW0gPSAoe3BhcmVudCwgaXRlbSwgbGV2ZWwsIC4uLnJlc3R9OiBhbnkpID0+IHtcbiAgICBpZiAoaXMoU3RyaW5nLCBpdGVtKSkge1xuICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgPFRyZWVWaWV3RWxlbWVudFxuICAgICAgICAgICAgICAgIGxhYmVsPXtpdGVtfVxuICAgICAgICAgICAgICAgIGlkZW50aWZpZXI9e3BhcmVudCA/IGpvaW4oJy4nLCBbcGFyZW50LCBpdGVtXSkgOiBpdGVtfVxuICAgICAgICAgICAgICAgIGxldmVsPXtsZXZlbCB8fCAwfVxuICAgICAgICAgICAgICAgIGtleT17aXRlbX1cbiAgICAgICAgICAgICAgICB7Li4ucmVzdH1cbiAgICAgICAgICAgIC8+XG4gICAgICAgICk7XG4gICAgfVxuICAgIHJldHVybiAoXG4gICAgICAgIDxUcmVlVmlld0VsZW1lbnRcbiAgICAgICAgICAgIHsuLi5pdGVtfVxuICAgICAgICAgICAgbGV2ZWw9e2xldmVsIHx8IDB9XG4gICAgICAgICAgICBrZXk9e2l0ZW0uaWRlbnRpZmllcn1cbiAgICAgICAgICAgIGlkZW50aWZpZXI9e1xuICAgICAgICAgICAgICAgIHBhcmVudCA/IGpvaW4oJy4nLCBbcGFyZW50LCBpdGVtLmlkZW50aWZpZXJdKSA6IGl0ZW0uaWRlbnRpZmllclxuICAgICAgICAgICAgfVxuICAgICAgICAgICAgey4uLnJlc3R9XG4gICAgICAgIC8+XG4gICAgKTtcbn07XG5cbi8qKlxuICogQSB0cmVlIG9mIG5lc3RlZCBpdGVtcy5cbiAqXG4gKiA6Q1NTOlxuICpcbiAqICAgICAtIGBgZGF6emxlci1leHRyYS10cmVlLXZpZXdgYFxuICogICAgIC0gYGB0cmVlLWl0ZW1gYFxuICogICAgIC0gYGB0cmVlLWl0ZW0tbGFiZWxgYFxuICogICAgIC0gYGB0cmVlLXN1Yi1pdGVtc2BgXG4gKiAgICAgLSBgYHRyZWUtY2FyZXRgYFxuICogICAgIC0gYGBzZWxlY3RlZGBgXG4gKiAgICAgLSBgYGxldmVsLXtufWBgXG4gKlxuICogOmV4YW1wbGU6XG4gKlxuICogLi4gbGl0ZXJhbGluY2x1ZGU6OiAuLi8uLi90ZXN0cy9jb21wb25lbnRzL3BhZ2VzL3RyZWV2aWV3LnB5XG4gKi9cbmNvbnN0IFRyZWVWaWV3ID0gKHtcbiAgICBjbGFzc19uYW1lLFxuICAgIHN0eWxlLFxuICAgIGlkZW50aXR5LFxuICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgaXRlbXMsXG4gICAgc2VsZWN0ZWQsXG4gICAgZXhwYW5kZWRfaXRlbXMsXG4gICAgbmVzdF9pY29uX2V4cGFuZGVkLFxuICAgIG5lc3RfaWNvbl9jb2xsYXBzZWQsXG59OiBUcmVlVmlld1Byb3BzKSA9PiB7XG4gICAgY29uc3Qgb25DbGljayA9IChlLCBpZGVudGlmaWVyLCBleHBhbmQpID0+IHtcbiAgICAgICAgZS5zdG9wUHJvcGFnYXRpb24oKTtcbiAgICAgICAgY29uc3QgcGF5bG9hZDogYW55ID0ge307XG4gICAgICAgIGlmIChzZWxlY3RlZCAmJiBpbmNsdWRlcyhpZGVudGlmaWVyLCBzZWxlY3RlZCkpIHtcbiAgICAgICAgICAgIGxldCBsYXN0ID0gc3BsaXQoJy4nLCBpZGVudGlmaWVyKTtcbiAgICAgICAgICAgIGxhc3QgPSBzbGljZSgwLCBsYXN0Lmxlbmd0aCAtIDEsIGxhc3QpO1xuICAgICAgICAgICAgaWYgKGxhc3QubGVuZ3RoID09PSAwKSB7XG4gICAgICAgICAgICAgICAgcGF5bG9hZC5zZWxlY3RlZCA9IG51bGw7XG4gICAgICAgICAgICB9IGVsc2UgaWYgKGxhc3QubGVuZ3RoID09PSAxKSB7XG4gICAgICAgICAgICAgICAgcGF5bG9hZC5zZWxlY3RlZCA9IGxhc3RbMF07XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgIHBheWxvYWQuc2VsZWN0ZWQgPSBqb2luKCcuJywgbGFzdCk7XG4gICAgICAgICAgICB9XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICBwYXlsb2FkLnNlbGVjdGVkID0gaWRlbnRpZmllcjtcbiAgICAgICAgfVxuXG4gICAgICAgIGlmIChleHBhbmQpIHtcbiAgICAgICAgICAgIGlmIChpbmNsdWRlcyhpZGVudGlmaWVyLCBleHBhbmRlZF9pdGVtcykpIHtcbiAgICAgICAgICAgICAgICBwYXlsb2FkLmV4cGFuZGVkX2l0ZW1zID0gd2l0aG91dChbaWRlbnRpZmllcl0sIGV4cGFuZGVkX2l0ZW1zKTtcbiAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgcGF5bG9hZC5leHBhbmRlZF9pdGVtcyA9IGNvbmNhdChleHBhbmRlZF9pdGVtcywgW2lkZW50aWZpZXJdKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgICB1cGRhdGVBc3BlY3RzKHBheWxvYWQpO1xuICAgIH07XG4gICAgcmV0dXJuIChcbiAgICAgICAgPGRpdiBjbGFzc05hbWU9e2NsYXNzX25hbWV9IHN0eWxlPXtzdHlsZX0gaWQ9e2lkZW50aXR5fT5cbiAgICAgICAgICAgIHtpdGVtcy5tYXAoKGl0ZW0pID0+XG4gICAgICAgICAgICAgICAgcmVuZGVySXRlbSh7XG4gICAgICAgICAgICAgICAgICAgIGl0ZW0sXG4gICAgICAgICAgICAgICAgICAgIG9uQ2xpY2ssXG4gICAgICAgICAgICAgICAgICAgIHNlbGVjdGVkLFxuICAgICAgICAgICAgICAgICAgICBuZXN0X2ljb25fZXhwYW5kZWQsXG4gICAgICAgICAgICAgICAgICAgIG5lc3RfaWNvbl9jb2xsYXBzZWQsXG4gICAgICAgICAgICAgICAgICAgIGV4cGFuZGVkX2l0ZW1zLFxuICAgICAgICAgICAgICAgIH0pXG4gICAgICAgICAgICApfVxuICAgICAgICA8L2Rpdj5cbiAgICApO1xufTtcblxuVHJlZVZpZXcuZGVmYXVsdFByb3BzID0ge1xuICAgIG5lc3RfaWNvbl9jb2xsYXBzZWQ6ICfij7UnLFxuICAgIG5lc3RfaWNvbl9leHBhbmRlZDogJ+KPtycsXG4gICAgZXhwYW5kZWRfaXRlbXM6IFtdLFxufTtcblxuZXhwb3J0IGRlZmF1bHQgVHJlZVZpZXc7XG4iLCJpbXBvcnQgJy4uL3Njc3MvaW5kZXguc2Nzcyc7XG5cbmltcG9ydCBOb3RpY2UgZnJvbSAnLi9jb21wb25lbnRzL05vdGljZSc7XG5pbXBvcnQgUGFnZXIgZnJvbSAnLi9jb21wb25lbnRzL1BhZ2VyJztcbmltcG9ydCBTcGlubmVyIGZyb20gJy4vY29tcG9uZW50cy9TcGlubmVyJztcbmltcG9ydCBTdGlja3kgZnJvbSAnLi9jb21wb25lbnRzL1N0aWNreSc7XG5pbXBvcnQgRHJhd2VyIGZyb20gJy4vY29tcG9uZW50cy9EcmF3ZXInO1xuaW1wb3J0IFBvcFVwIGZyb20gJy4vY29tcG9uZW50cy9Qb3BVcCc7XG5pbXBvcnQgVHJlZVZpZXcgZnJvbSAnLi9jb21wb25lbnRzL1RyZWVWaWV3JztcbmltcG9ydCBUb2FzdCBmcm9tICcuL2NvbXBvbmVudHMvVG9hc3QnO1xuaW1wb3J0IFBhZ2VNYXAgZnJvbSAnLi9jb21wb25lbnRzL1BhZ2VNYXAnO1xuXG5leHBvcnQge1xuICAgIE5vdGljZSxcbiAgICBQYWdlcixcbiAgICBTcGlubmVyLFxuICAgIFN0aWNreSxcbiAgICBEcmF3ZXIsXG4gICAgUG9wVXAsXG4gICAgVHJlZVZpZXcsXG4gICAgVG9hc3QsXG4gICAgUGFnZU1hcCxcbn07XG4iLCJtb2R1bGUuZXhwb3J0cyA9IF9fV0VCUEFDS19FWFRFUk5BTF9NT0RVTEVfcmVhY3RfXzsiXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=