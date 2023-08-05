"use strict";
(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory(require("react"), require("react-dom"));
	else if(typeof define === 'function' && define.amd)
		define(["react", "react-dom"], factory);
	else if(typeof exports === 'object')
		exports["dazzler_renderer"] = factory(require("react"), require("react-dom"));
	else
		root["dazzler_renderer"] = factory(root["React"], root["ReactDOM"]);
})(self, function(__WEBPACK_EXTERNAL_MODULE_react__, __WEBPACK_EXTERNAL_MODULE_react_dom__) {
return (self["webpackChunkdazzler_name_"] = self["webpackChunkdazzler_name_"] || []).push([["renderer"],{

/***/ "./src/renderer/js/components/Renderer.tsx":
/*!*************************************************!*\
  !*** ./src/renderer/js/components/Renderer.tsx ***!
  \*************************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
var react_1 = __importStar(__webpack_require__(/*! react */ "react"));
var Updater_1 = __importDefault(__webpack_require__(/*! ./Updater */ "./src/renderer/js/components/Updater.tsx"));
var Renderer = function (props) {
    var _a = react_1.useState(1), reloadKey = _a[0], setReloadKey = _a[1];
    // FIXME find where this is used and refactor/remove
    // @ts-ignore
    window.dazzler_base_url = props.baseUrl;
    return (react_1["default"].createElement("div", { className: "dazzler-renderer" },
        react_1["default"].createElement(Updater_1["default"], __assign({}, props, { key: "upd-" + reloadKey, hotReload: function () { return setReloadKey(reloadKey + 1); } }))));
};
exports.default = Renderer;


/***/ }),

/***/ "./src/renderer/js/components/Updater.tsx":
/*!************************************************!*\
  !*** ./src/renderer/js/components/Updater.tsx ***!
  \************************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
var requests_1 = __webpack_require__(/*! ../requests */ "./src/renderer/js/requests.ts");
var hydrator_1 = __webpack_require__(/*! ../hydrator */ "./src/renderer/js/hydrator.tsx");
var requirements_1 = __webpack_require__(/*! ../requirements */ "./src/renderer/js/requirements.ts");
var commons_1 = __webpack_require__(/*! commons */ "./src/commons/js/index.ts");
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var transforms_1 = __webpack_require__(/*! ../transforms */ "./src/renderer/js/transforms.ts");
var Updater = /** @class */ (function (_super) {
    __extends(Updater, _super);
    function Updater(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            layout: null,
            ready: false,
            page: null,
            bindings: {},
            packages: [],
            reload: false,
            rebindings: [],
            requirements: [],
            reloading: false,
            needRefresh: false,
            ties: {},
        };
        // The api url for the page is the same but a post.
        // Fetch bindings, packages & requirements
        _this.pageApi = requests_1.apiRequest(window.location.href);
        // All components get connected.
        _this.boundComponents = {};
        _this.ws = null;
        _this.updateAspects = _this.updateAspects.bind(_this);
        _this.connect = _this.connect.bind(_this);
        _this.disconnect = _this.disconnect.bind(_this);
        _this.onMessage = _this.onMessage.bind(_this);
        return _this;
    }
    Updater.prototype.updateAspects = function (identity, aspects) {
        var _this = this;
        return new Promise(function (resolve) {
            var aspectKeys = ramda_1.keys(aspects);
            var bindings = aspectKeys
                .map(function (key) { return (__assign(__assign({}, _this.state.bindings[key + "@" + identity]), { value: aspects[key] })); })
                .filter(function (e) { return e.trigger; });
            _this.state.rebindings.forEach(function (binding) {
                if (binding.trigger.identity.test(identity)) {
                    // @ts-ignore
                    bindings = ramda_1.concat(bindings, aspectKeys
                        .filter(function (k) {
                        return binding.trigger.aspect.test(k);
                    })
                        .map(function (k) { return (__assign(__assign({}, binding), { value: aspects[k], trigger: __assign(__assign({}, binding.trigger), { identity: identity, aspect: k }) })); }));
                }
            });
            ramda_1.flatten(aspectKeys.map(function (key) {
                var ties = [];
                for (var i = 0; i < _this.state.ties.length; i++) {
                    var tie = _this.state.ties[i];
                    var trigger = tie.trigger;
                    if ((trigger.regex &&
                        trigger.identity.test(identity) &&
                        trigger.aspect.test(key)) ||
                        (trigger.identity === identity &&
                            trigger.aspect === key)) {
                        ties.push(__assign(__assign({}, tie), { value: aspects[key] }));
                    }
                }
                return ties;
            })).forEach(function (tie) {
                var transforms = tie.transforms;
                var value = tie.value;
                if (transforms) {
                    value = transforms.reduce(function (acc, e) {
                        return transforms_1.executeTransform(e.transform, acc, e.args, e.next, _this.getAspect.bind(_this));
                    }, value);
                }
                tie.targets.forEach(function (t) {
                    var _a;
                    var component = _this.boundComponents[t.identity];
                    if (component) {
                        component.updateAspects((_a = {}, _a[t.aspect] = value, _a));
                    }
                });
            });
            if (!bindings) {
                resolve(0);
            }
            else {
                bindings.forEach(function (binding) {
                    return _this.sendBinding(binding, binding.value);
                });
                resolve(bindings.length);
            }
        });
    };
    Updater.prototype.getAspect = function (identity, aspect) {
        var c = this.boundComponents[identity];
        if (c) {
            return c.getAspect(aspect);
        }
        return undefined;
    };
    Updater.prototype.connect = function (identity, setAspects, getAspect, matchAspects, updateAspects) {
        this.boundComponents[identity] = {
            setAspects: setAspects,
            getAspect: getAspect,
            matchAspects: matchAspects,
            updateAspects: updateAspects,
        };
    };
    Updater.prototype.disconnect = function (identity) {
        delete this.boundComponents[identity];
    };
    Updater.prototype.onMessage = function (response) {
        var _this = this;
        var data = JSON.parse(response.data);
        var identity = data.identity, kind = data.kind, payload = data.payload, storage = data.storage, request_id = data.request_id;
        var store;
        if (storage === 'session') {
            store = window.sessionStorage;
        }
        else {
            store = window.localStorage;
        }
        switch (kind) {
            case 'set-aspect':
                var setAspects = function (component) {
                    return component
                        .setAspects(hydrator_1.hydrateProps(payload, _this.updateAspects, _this.connect, _this.disconnect))
                        .then(function () { return _this.updateAspects(identity, payload); });
                };
                if (data.regex) {
                    var pattern_1 = new RegExp(data.identity);
                    ramda_1.keys(this.boundComponents)
                        .filter(function (k) { return pattern_1.test(k); })
                        .map(function (k) { return _this.boundComponents[k]; })
                        .forEach(setAspects);
                }
                else {
                    setAspects(this.boundComponents[identity]);
                }
                break;
            case 'get-aspect':
                var aspect = data.aspect;
                var wanted = this.boundComponents[identity];
                if (!wanted) {
                    this.ws.send(JSON.stringify({
                        kind: kind,
                        identity: identity,
                        aspect: aspect,
                        request_id: request_id,
                        error: "Aspect not found " + identity + "." + aspect,
                    }));
                    return;
                }
                var value = wanted.getAspect(aspect);
                this.ws.send(JSON.stringify({
                    kind: kind,
                    identity: identity,
                    aspect: aspect,
                    value: hydrator_1.prepareProp(value),
                    request_id: request_id,
                }));
                break;
            case 'set-storage':
                store.setItem(identity, JSON.stringify(payload));
                break;
            case 'get-storage':
                this.ws.send(JSON.stringify({
                    kind: kind,
                    identity: identity,
                    request_id: request_id,
                    value: JSON.parse(store.getItem(identity)),
                }));
                break;
            case 'reload':
                var filenames = data.filenames, hot = data.hot, refresh = data.refresh, deleted = data.deleted;
                if (refresh) {
                    this.ws.close();
                    this.setState({ reloading: true, needRefresh: true });
                    return;
                }
                if (hot) {
                    // The ws connection will close, when it
                    // reconnect it will do a hard reload of the page api.
                    this.setState({ reloading: true });
                    return;
                }
                filenames.forEach(requirements_1.loadRequirement);
                deleted.forEach(function (r) { return commons_1.disableCss(r.url); });
                break;
            case 'ping':
                // Just do nothing.
                break;
        }
    };
    Updater.prototype.sendBinding = function (binding, value) {
        var _this = this;
        // Collect all values and send a binding payload
        var trigger = __assign(__assign({}, binding.trigger), { value: hydrator_1.prepareProp(value) });
        var states = binding.states.reduce(function (acc, state) {
            if (state.regex) {
                var identityPattern_1 = new RegExp(state.identity);
                var aspectPattern_1 = new RegExp(state.aspect);
                return ramda_1.concat(acc, ramda_1.flatten(ramda_1.keys(_this.boundComponents).map(function (k) {
                    var values = [];
                    if (identityPattern_1.test(k)) {
                        values = _this.boundComponents[k]
                            .matchAspects(aspectPattern_1)
                            .map(function (_a) {
                            var name = _a[0], val = _a[1];
                            return (__assign(__assign({}, state), { identity: k, aspect: name, value: hydrator_1.prepareProp(val) }));
                        });
                    }
                    return values;
                })));
            }
            acc.push(__assign(__assign({}, state), { value: _this.boundComponents[state.identity] &&
                    hydrator_1.prepareProp(_this.boundComponents[state.identity].getAspect(state.aspect)) }));
            return acc;
        }, []);
        var payload = {
            trigger: trigger,
            states: states,
            kind: 'binding',
            page: this.state.page,
            key: binding.key,
        };
        this.ws.send(JSON.stringify(payload));
    };
    Updater.prototype._connectWS = function () {
        var _this = this;
        // Setup websocket for updates
        var tries = 0;
        var hardClose = false;
        var connexion = function () {
            var url = "ws" + (window.location.href.startsWith('https') ? 's' : '') + "://" + ((_this.props.baseUrl && _this.props.baseUrl) ||
                window.location.host) + "/" + _this.state.page + "/ws";
            _this.ws = new WebSocket(url);
            _this.ws.addEventListener('message', _this.onMessage);
            _this.ws.onopen = function () {
                if (_this.state.reloading) {
                    hardClose = true;
                    _this.ws.close();
                    if (_this.state.needRefresh) {
                        window.location.reload();
                    }
                    else {
                        _this.props.hotReload();
                    }
                }
                else {
                    _this.setState({ ready: true });
                    tries = 0;
                }
            };
            _this.ws.onclose = function () {
                var reconnect = function () {
                    tries++;
                    connexion();
                };
                if (!hardClose && tries < _this.props.retries) {
                    setTimeout(reconnect, 1000);
                }
            };
        };
        connexion();
    };
    Updater.prototype.componentDidMount = function () {
        var _this = this;
        this.pageApi('', { method: 'POST' }).then(function (response) {
            var toRegex = function (x) { return new RegExp(x); };
            _this.setState({
                page: response.page,
                layout: response.layout,
                bindings: ramda_1.pickBy(function (b) { return !b.regex; }, response.bindings),
                // Regex bindings triggers
                rebindings: ramda_1.map(function (x) {
                    var binding = response.bindings[x];
                    binding.trigger = ramda_1.evolve({
                        identity: toRegex,
                        aspect: toRegex,
                    }, binding.trigger);
                    return binding;
                }, ramda_1.keys(ramda_1.pickBy(function (b) { return b.regex; }, response.bindings))),
                packages: response.packages,
                requirements: response.requirements,
                ties: ramda_1.map(function (tie) {
                    if (tie.trigger.regex) {
                        return ramda_1.evolve({
                            trigger: {
                                identity: toRegex,
                                aspect: toRegex,
                            },
                        }, tie);
                    }
                    return tie;
                }, response.ties),
            }, function () {
                return requirements_1.loadRequirements(response.requirements, response.packages).then(function () {
                    if (ramda_1.keys(response.bindings).length || response.reload) {
                        _this._connectWS();
                    }
                    else {
                        _this.setState({ ready: true });
                    }
                });
            });
        });
    };
    Updater.prototype.render = function () {
        var _a = this.state, layout = _a.layout, ready = _a.ready, reloading = _a.reloading;
        if (!ready) {
            return (react_1["default"].createElement("div", { className: "dazzler-loading-container" },
                react_1["default"].createElement("div", { className: "dazzler-spin" }),
                react_1["default"].createElement("div", { className: "dazzler-loading" }, "Loading...")));
        }
        if (reloading) {
            return (react_1["default"].createElement("div", { className: "dazzler-loading-container" },
                react_1["default"].createElement("div", { className: "dazzler-spin reload" }),
                react_1["default"].createElement("div", { className: "dazzler-loading" }, "Reloading...")));
        }
        if (!hydrator_1.isComponent(layout)) {
            throw new Error("Layout is not a component: " + layout);
        }
        var contexts = [];
        var onContext = function (contextComponent) {
            contexts.push(contextComponent);
        };
        var hydrated = hydrator_1.hydrateComponent(layout.name, layout.package, layout.identity, hydrator_1.hydrateProps(layout.aspects, this.updateAspects, this.connect, this.disconnect, onContext), this.updateAspects, this.connect, this.disconnect, onContext);
        return (react_1["default"].createElement("div", { className: "dazzler-rendered" }, contexts.length
            ? contexts.reduce(function (acc, Context) {
                if (!acc) {
                    return react_1["default"].createElement(Context, null, hydrated);
                }
                return react_1["default"].createElement(Context, null, acc);
            }, null)
            : hydrated));
    };
    return Updater;
}(react_1["default"].Component));
exports.default = Updater;


/***/ }),

/***/ "./src/renderer/js/components/Wrapper.tsx":
/*!************************************************!*\
  !*** ./src/renderer/js/components/Wrapper.tsx ***!
  \************************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var commons_1 = __webpack_require__(/*! commons */ "./src/commons/js/index.ts");
/**
 * Wraps components for aspects updating.
 */
var Wrapper = /** @class */ (function (_super) {
    __extends(Wrapper, _super);
    function Wrapper(props) {
        var _this = _super.call(this, props) || this;
        _this.state = {
            aspects: props.aspects || {},
            ready: false,
            initial: false,
        };
        _this.setAspects = _this.setAspects.bind(_this);
        _this.getAspect = _this.getAspect.bind(_this);
        _this.updateAspects = _this.updateAspects.bind(_this);
        _this.matchAspects = _this.matchAspects.bind(_this);
        return _this;
    }
    Wrapper.prototype.updateAspects = function (aspects) {
        var _this = this;
        return this.setAspects(aspects).then(function () {
            return _this.props.updateAspects(_this.props.identity, aspects);
        });
    };
    Wrapper.prototype.setAspects = function (aspects) {
        var _this = this;
        return new Promise(function (resolve) {
            _this.setState({ aspects: __assign(__assign({}, _this.state.aspects), aspects) }, resolve);
        });
    };
    Wrapper.prototype.getAspect = function (aspect) {
        return this.state.aspects[aspect];
    };
    Wrapper.prototype.matchAspects = function (pattern) {
        var _this = this;
        return ramda_1.keys(this.state.aspects)
            .filter(function (k) { return pattern.test(k); })
            .map(function (k) { return [k, _this.state.aspects[k]]; });
    };
    Wrapper.prototype.componentDidMount = function () {
        var _this = this;
        // Only update the component when mounted.
        // Otherwise gets a race condition with willUnmount
        this.props.connect(this.props.identity, this.setAspects, this.getAspect, this.matchAspects, this.updateAspects);
        if (!this.state.initial) {
            this.updateAspects(this.state.aspects).then(function () {
                return _this.setState({ ready: true, initial: true });
            });
        }
    };
    Wrapper.prototype.componentWillUnmount = function () {
        this.props.disconnect(this.props.identity);
    };
    Wrapper.prototype.render = function () {
        var _a = this.props, component = _a.component, component_name = _a.component_name, package_name = _a.package_name;
        var _b = this.state, aspects = _b.aspects, ready = _b.ready;
        if (!ready) {
            return null;
        }
        return react_1["default"].cloneElement(component, __assign(__assign({}, aspects), { updateAspects: this.updateAspects, identity: this.props.identity, class_name: ramda_1.join(' ', ramda_1.concat([
                package_name
                    .replace('_', '-')
                    .toLowerCase() + "-" + commons_1.camelToSpinal(component_name),
            ], aspects.class_name ? aspects.class_name.split(' ') : [])) }));
    };
    return Wrapper;
}(react_1["default"].Component));
exports.default = Wrapper;


/***/ }),

/***/ "./src/renderer/js/hydrator.tsx":
/*!**************************************!*\
  !*** ./src/renderer/js/hydrator.tsx ***!
  \**************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
exports.prepareProp = exports.hydrateComponent = exports.hydrateProps = exports.isComponent = void 0;
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var Wrapper_1 = __importDefault(__webpack_require__(/*! ./components/Wrapper */ "./src/renderer/js/components/Wrapper.tsx"));
function isComponent(c) {
    return (ramda_1.type(c) === 'Object' &&
        c.hasOwnProperty('package') &&
        c.hasOwnProperty('aspects') &&
        c.hasOwnProperty('name') &&
        c.hasOwnProperty('identity'));
}
exports.isComponent = isComponent;
function hydrateProps(props, updateAspects, connect, disconnect, onContext) {
    var replace = {};
    Object.entries(props).forEach(function (_a) {
        var k = _a[0], v = _a[1];
        if (ramda_1.type(v) === 'Array') {
            replace[k] = v.map(function (c) {
                if (!isComponent(c)) {
                    // Mixing components and primitives
                    if (ramda_1.type(c) === 'Object') {
                        // Not a component but maybe it contains some ?
                        return hydrateProps(c, updateAspects, connect, disconnect, onContext);
                    }
                    return c;
                }
                var newProps = hydrateProps(c.aspects, updateAspects, connect, disconnect, onContext);
                if (!newProps.key) {
                    newProps.key = c.identity;
                }
                return hydrateComponent(c.name, c.package, c.identity, newProps, updateAspects, connect, disconnect, onContext);
            });
        }
        else if (isComponent(v)) {
            var newProps = hydrateProps(v.aspects, updateAspects, connect, disconnect, onContext);
            replace[k] = hydrateComponent(v.name, v.package, v.identity, newProps, updateAspects, connect, disconnect, onContext);
        }
        else if (ramda_1.type(v) === 'Object') {
            replace[k] = hydrateProps(v, updateAspects, connect, disconnect, onContext);
        }
    });
    return __assign(__assign({}, props), replace);
}
exports.hydrateProps = hydrateProps;
function hydrateComponent(name, package_name, identity, props, updateAspects, connect, disconnect, onContext) {
    var pack = window[package_name];
    if (!pack) {
        throw new Error("Invalid package name: " + package_name);
    }
    var component = pack[name];
    if (!component) {
        throw new Error("Invalid component name: " + package_name + "." + name);
    }
    // @ts-ignore
    var element = react_1["default"].createElement(component, props);
    /* eslint-disable react/prop-types */
    var wrapper = function (_a) {
        var children = _a.children;
        return (react_1["default"].createElement(Wrapper_1["default"], { identity: identity, updateAspects: updateAspects, component: element, connect: connect, package_name: package_name, component_name: name, aspects: __assign({ children: children }, props), disconnect: disconnect, key: "wrapper-" + identity }));
    };
    if (component.isContext) {
        onContext(wrapper);
        return null;
    }
    return wrapper({});
}
exports.hydrateComponent = hydrateComponent;
function prepareProp(prop) {
    if (react_1["default"].isValidElement(prop)) {
        // @ts-ignore
        var props = prop.props;
        return {
            identity: props.identity,
            // @ts-ignore
            aspects: ramda_1.map(prepareProp, ramda_1.omit([
                'identity',
                'updateAspects',
                '_name',
                '_package',
                'aspects',
                'key',
            ], props.aspects)),
            name: props.component_name,
            package: props.package_name,
        };
    }
    if (ramda_1.type(prop) === 'Array') {
        return prop.map(prepareProp);
    }
    if (ramda_1.type(prop) === 'Object') {
        return ramda_1.map(prepareProp, prop);
    }
    return prop;
}
exports.prepareProp = prepareProp;


/***/ }),

/***/ "./src/renderer/js/index.tsx":
/*!***********************************!*\
  !*** ./src/renderer/js/index.tsx ***!
  \***********************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
exports.__esModule = true;
exports.render = exports.Renderer = void 0;
var react_1 = __importDefault(__webpack_require__(/*! react */ "react"));
var react_dom_1 = __importDefault(__webpack_require__(/*! react-dom */ "react-dom"));
var Renderer_1 = __importDefault(__webpack_require__(/*! ./components/Renderer */ "./src/renderer/js/components/Renderer.tsx"));
exports.Renderer = Renderer_1["default"];
function render(_a, element) {
    var baseUrl = _a.baseUrl, ping = _a.ping, ping_interval = _a.ping_interval, retries = _a.retries;
    react_dom_1["default"].render(react_1["default"].createElement(Renderer_1["default"], { baseUrl: baseUrl, ping: ping, ping_interval: ping_interval, retries: retries }), element);
}
exports.render = render;


/***/ }),

/***/ "./src/renderer/js/requests.ts":
/*!*************************************!*\
  !*** ./src/renderer/js/requests.ts ***!
  \*************************************/
/***/ (function(__unused_webpack_module, exports) {


/* eslint-disable no-magic-numbers */
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
exports.__esModule = true;
exports.apiRequest = exports.xhrRequest = exports.JSONHEADERS = void 0;
var jsonPattern = /json/i;
var defaultXhrOptions = {
    method: 'GET',
    headers: {},
    payload: '',
    json: true,
};
exports.JSONHEADERS = {
    'Content-Type': 'application/json',
};
function xhrRequest(url, options) {
    if (options === void 0) { options = defaultXhrOptions; }
    return new Promise(function (resolve, reject) {
        var _a = __assign(__assign({}, defaultXhrOptions), options), method = _a.method, headers = _a.headers, payload = _a.payload, json = _a.json;
        var xhr = new XMLHttpRequest();
        xhr.open(method, url);
        var head = json ? __assign(__assign({}, exports.JSONHEADERS), headers) : headers;
        Object.keys(head).forEach(function (k) { return xhr.setRequestHeader(k, head[k]); });
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var responseValue = xhr.response;
                    if (jsonPattern.test(xhr.getResponseHeader('Content-Type'))) {
                        responseValue = JSON.parse(xhr.responseText);
                    }
                    resolve(responseValue);
                }
                else {
                    reject({
                        error: 'RequestError',
                        message: "XHR " + url + " FAILED - STATUS: " + xhr.status + " MESSAGE: " + xhr.statusText,
                        status: xhr.status,
                        xhr: xhr,
                    });
                }
            }
        };
        xhr.onerror = function (err) { return reject(err); };
        // @ts-ignore
        xhr.send(json ? JSON.stringify(payload) : payload);
    });
}
exports.xhrRequest = xhrRequest;
function apiRequest(baseUrl) {
    return function () {
        var url = baseUrl + arguments[0];
        var options = arguments[1] || {};
        options.headers = __assign({}, options.headers);
        return new Promise(function (resolve) {
            xhrRequest(url, options).then(resolve);
        });
    };
}
exports.apiRequest = apiRequest;


/***/ }),

/***/ "./src/renderer/js/requirements.ts":
/*!*****************************************!*\
  !*** ./src/renderer/js/requirements.ts ***!
  \*****************************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


exports.__esModule = true;
exports.loadRequirements = exports.loadRequirement = void 0;
var commons_1 = __webpack_require__(/*! commons */ "./src/commons/js/index.ts");
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
function loadRequirement(requirement) {
    return new Promise(function (resolve, reject) {
        var url = requirement.url, kind = requirement.kind;
        var method;
        if (kind === 'js') {
            method = commons_1.loadScript;
        }
        else if (kind === 'css') {
            method = commons_1.loadCss;
        }
        else if (kind === 'map') {
            return resolve();
        }
        else {
            return reject({ error: "Invalid requirement kind: " + kind });
        }
        return method(url).then(resolve)["catch"](reject);
    });
}
exports.loadRequirement = loadRequirement;
function loadOneByOne(requirements) {
    return new Promise(function (resolve) {
        var handle = function (reqs) {
            if (reqs.length) {
                var requirement = reqs[0];
                loadRequirement(requirement).then(function () { return handle(ramda_1.drop(1, reqs)); });
            }
            else {
                resolve(null);
            }
        };
        handle(requirements);
    });
}
function loadRequirements(requirements, packages) {
    return new Promise(function (resolve, reject) {
        var loadings = [];
        Object.keys(packages).forEach(function (pack_name) {
            var pack = packages[pack_name];
            loadings = loadings.concat(loadOneByOne(pack.requirements.filter(function (r) { return r.kind === 'js'; })));
            loadings = loadings.concat(pack.requirements
                .filter(function (r) { return r.kind === 'css'; })
                .map(loadRequirement));
        });
        // Then load requirements so they can use packages
        // and override css.
        Promise.all(loadings)
            .then(function () {
            var i = 0;
            // Load in order.
            var handler = function () {
                if (i < requirements.length) {
                    loadRequirement(requirements[i]).then(function () {
                        i++;
                        handler();
                    });
                }
                else {
                    resolve();
                }
            };
            handler();
        })["catch"](reject);
    });
}
exports.loadRequirements = loadRequirements;


/***/ }),

/***/ "./src/renderer/js/transforms.ts":
/*!***************************************!*\
  !*** ./src/renderer/js/transforms.ts ***!
  \***************************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


exports.__esModule = true;
exports.executeTransform = void 0;
/* eslint-disable no-use-before-define */
var ramda_1 = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
var isAspect = function (obj) {
    return ramda_1.is(Object, obj) && ramda_1.has('identity', obj) && ramda_1.has('aspect', obj);
};
var coerceAspect = function (obj, getAspect) {
    return isAspect(obj) ? getAspect(obj.identity, obj.aspect) : obj;
};
var transforms = {
    /* String transforms */
    ToUpper: function (value) {
        return value.toUpperCase();
    },
    ToLower: function (value) {
        return value.toLowerCase();
    },
    Format: function (value, args) {
        var template = args.template;
        if (ramda_1.is(String, value) || ramda_1.is(Number, value) || ramda_1.is(Boolean, value)) {
            return ramda_1.replace('${value}', value, template);
        }
        else if (ramda_1.is(Object, value)) {
            return ramda_1.reduce(function (acc, _a) {
                var k = _a[0], v = _a[1];
                return ramda_1.replace("${" + k + "}", v, acc);
            }, template, ramda_1.toPairs(value));
        }
        return value;
    },
    Split: function (value, args) {
        var separator = args.separator;
        return ramda_1.split(separator, value);
    },
    Trim: function (value) {
        return ramda_1.trim(value);
    },
    /* Number Transform */
    Add: function (value, args, getAspect) {
        if (ramda_1.is(Number, args.value)) {
            return value + args.value;
        }
        return value + coerceAspect(args.value, getAspect);
    },
    Sub: function (value, args, getAspect) {
        if (ramda_1.is(Number, args.value)) {
            return value - args.value;
        }
        return value - coerceAspect(args.value, getAspect);
    },
    Divide: function (value, args, getAspect) {
        if (ramda_1.is(Number, args.value)) {
            return value / args.value;
        }
        return value / coerceAspect(args.value, getAspect);
    },
    Multiply: function (value, args, getAspect) {
        if (ramda_1.is(Number, args.value)) {
            return value * args.value;
        }
        return value * coerceAspect(args.value, getAspect);
    },
    Modulus: function (value, args, getAspect) {
        if (ramda_1.is(Number, args.value)) {
            return value % args.value;
        }
        return value % coerceAspect(args.value, getAspect);
    },
    ToPrecision: function (value, args) {
        return value.toPrecision(args.precision);
    },
    /* Array transforms  */
    Concat: function (value, args, getAspect) {
        var other = args.other;
        return ramda_1.concat(value, coerceAspect(other, getAspect));
    },
    Slice: function (value, args) {
        return ramda_1.slice(args.start, args.stop, value);
    },
    Map: function (value, args, getAspect) {
        var transform = args.transform;
        return value.map(function (e) {
            return exports.executeTransform(transform.transform, e, transform.args, transform.next, getAspect);
        });
    },
    Filter: function (value, args, getAspect) {
        var comparison = args.comparison;
        return value.filter(function (e) {
            return exports.executeTransform(comparison.transform, e, comparison.args, comparison.next, getAspect);
        });
    },
    Reduce: function (value, args, getAspect) {
        var transform = args.transform, accumulator = args.accumulator;
        var acc = coerceAspect(accumulator, getAspect);
        return value.reduce(function (previous, next) {
            return exports.executeTransform(transform.transform, [previous, next], transform.args, transform.next, getAspect);
        }, acc);
    },
    Pluck: function (value, args) {
        var field = args.field;
        return ramda_1.pluck(field, value);
    },
    Append: function (value, args, getAspect) {
        return ramda_1.concat(value, [coerceAspect(args.value, getAspect)]);
    },
    Prepend: function (value, args, getAspect) {
        return ramda_1.concat([coerceAspect(args.value, getAspect)], value);
    },
    Insert: function (value, args, getAspect) {
        var target = args.target, front = args.front;
        var t = coerceAspect(target, getAspect);
        return front ? ramda_1.concat([value], t) : ramda_1.concat(t, [value]);
    },
    Take: function (value, args, getAspect) {
        var n = args.n;
        return ramda_1.take(coerceAspect(n, getAspect), value);
    },
    Length: function (value) {
        return value.length;
    },
    Range: function (value, args, getAspect) {
        var start = args.start, end = args.end, step = args.step;
        var s = coerceAspect(start, getAspect);
        var e = coerceAspect(end, getAspect);
        var i = s;
        var arr = [];
        while (i < e) {
            arr.push(i);
            i += step;
        }
        return arr;
    },
    Includes: function (value, args, getAspect) {
        return ramda_1.includes(coerceAspect(args.value, getAspect), value);
    },
    Find: function (value, args, getAspect) {
        var comparison = args.comparison;
        return ramda_1.find(function (a) {
            return exports.executeTransform(comparison.transform, a, comparison.args, comparison.next, getAspect);
        })(value);
    },
    Join: function (value, args, getAspect) {
        return ramda_1.join(coerceAspect(args.separator, getAspect), value);
    },
    Sort: function (value, args, getAspect) {
        var transform = args.transform;
        return ramda_1.sort(function (a, b) {
            return exports.executeTransform(transform.transform, [a, b], transform.args, transform.next, getAspect);
        }, value);
    },
    Reverse: function (value) {
        return ramda_1.reverse(value);
    },
    Unique: function (value) {
        return ramda_1.uniq(value);
    },
    Zip: function (value, args, getAspect) {
        return ramda_1.zip(value, coerceAspect(args.value, getAspect));
    },
    /* Object transforms */
    Pick: function (value, args) {
        return ramda_1.pick(args.fields, value);
    },
    Get: function (value, args) {
        return value[args.field];
    },
    Set: function (v, args, getAspect) {
        var key = args.key, value = args.value;
        v[key] = coerceAspect(value, getAspect);
        return v;
    },
    Put: function (value, args, getAspect) {
        var key = args.key, target = args.target;
        var obj = coerceAspect(target, getAspect);
        obj[key] = value;
        return obj;
    },
    Merge: function (value, args, getAspect) {
        var deep = args.deep, direction = args.direction, other = args.other;
        var otherValue = other;
        if (isAspect(other)) {
            otherValue = getAspect(other.identity, other.aspect);
        }
        if (direction === 'right') {
            if (deep) {
                return ramda_1.mergeDeepRight(value, otherValue);
            }
            return ramda_1.mergeRight(value, otherValue);
        }
        if (deep) {
            return ramda_1.mergeDeepLeft(value, otherValue);
        }
        return ramda_1.mergeLeft(value, otherValue);
    },
    ToJson: function (value) {
        return JSON.stringify(value);
    },
    FromJson: function (value) {
        return JSON.parse(value);
    },
    ToPairs: function (value) {
        return ramda_1.toPairs(value);
    },
    FromPairs: function (value) {
        return ramda_1.fromPairs(value);
    },
    /* Conditionals */
    If: function (value, args, getAspect) {
        var comparison = args.comparison, then = args.then, otherwise = args.otherwise;
        var c = transforms[comparison.transform];
        if (c(value, comparison.args, getAspect)) {
            return exports.executeTransform(then.transform, value, then.args, then.next, getAspect);
        }
        if (otherwise) {
            return exports.executeTransform(otherwise.transform, value, otherwise.args, otherwise.next, getAspect);
        }
        return value;
    },
    Equals: function (value, args, getAspect) {
        return ramda_1.equals(value, coerceAspect(args.other, getAspect));
    },
    NotEquals: function (value, args, getAspect) {
        return !ramda_1.equals(value, coerceAspect(args.other, getAspect));
    },
    Match: function (value, args, getAspect) {
        var r = new RegExp(coerceAspect(args.other, getAspect));
        return r.test(value);
    },
    Greater: function (value, args, getAspect) {
        return value > coerceAspect(args.other, getAspect);
    },
    GreaterOrEquals: function (value, args, getAspect) {
        return value >= coerceAspect(args.other, getAspect);
    },
    Lesser: function (value, args, getAspect) {
        return value < coerceAspect(args.other, getAspect);
    },
    LesserOrEquals: function (value, args, getAspect) {
        return value <= coerceAspect(args.other, getAspect);
    },
    And: function (value, args, getAspect) {
        return value && coerceAspect(args.other, getAspect);
    },
    Or: function (value, args, getAspect) {
        return value || coerceAspect(args.other, getAspect);
    },
    Not: function (value) {
        return !value;
    },
    RawValue: function (value, args) {
        return args.value;
    },
    AspectValue: function (value, args, getAspect) {
        var _a = args.target, identity = _a.identity, aspect = _a.aspect;
        return getAspect(identity, aspect);
    },
};
var executeTransform = function (transform, value, args, next, getAspect) {
    var t = transforms[transform];
    var newValue = t(value, args, getAspect);
    if (next.length) {
        var n = next[0];
        return exports.executeTransform(n.transform, newValue, n.args, 
        // Execute the next first, then back to chain.
        ramda_1.concat(n.next, ramda_1.drop(1, next)), getAspect);
    }
    return newValue;
};
exports.executeTransform = executeTransform;
exports.default = transforms;


/***/ }),

/***/ "react":
/*!****************************************************************************************************!*\
  !*** external {"commonjs":"react","commonjs2":"react","amd":"react","umd":"react","root":"React"} ***!
  \****************************************************************************************************/
/***/ ((module) => {

module.exports = __WEBPACK_EXTERNAL_MODULE_react__;

/***/ }),

/***/ "react-dom":
/*!***********************************************************************************************************************!*\
  !*** external {"commonjs":"react-dom","commonjs2":"react-dom","amd":"react-dom","umd":"react-dom","root":"ReactDOM"} ***!
  \***********************************************************************************************************************/
/***/ ((module) => {

module.exports = __WEBPACK_EXTERNAL_MODULE_react_dom__;

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ var __webpack_exports__ = (__webpack_exec__("./src/renderer/js/index.tsx"));
/******/ return __webpack_exports__;
/******/ }
]);
});
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGF6emxlcl9yZW5kZXJlcl84MmI3MDc0MzY0ODRlODVmY2I0MS5qcyIsIm1hcHBpbmdzIjoiO0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsQ0FBQztBQUNELE87Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNWQSxzRUFBc0M7QUFDdEMsa0hBQWdDO0FBSWhDLElBQU0sUUFBUSxHQUFHLFVBQUMsS0FBb0I7SUFDNUIsU0FBNEIsZ0JBQVEsQ0FBQyxDQUFDLENBQUMsRUFBdEMsU0FBUyxVQUFFLFlBQVksUUFBZSxDQUFDO0lBRTlDLG9EQUFvRDtJQUNwRCxhQUFhO0lBQ2IsTUFBTSxDQUFDLGdCQUFnQixHQUFHLEtBQUssQ0FBQyxPQUFPLENBQUM7SUFDeEMsT0FBTyxDQUNILDBDQUFLLFNBQVMsRUFBQyxrQkFBa0I7UUFDN0IsaUNBQUMsb0JBQU8sZUFDQSxLQUFLLElBQ1QsR0FBRyxFQUFFLFNBQU8sU0FBVyxFQUN2QixTQUFTLEVBQUUsY0FBTSxtQkFBWSxDQUFDLFNBQVMsR0FBRyxDQUFDLENBQUMsRUFBM0IsQ0FBMkIsSUFDOUMsQ0FDQSxDQUNULENBQUM7QUFDTixDQUFDLENBQUM7QUFFRixrQkFBZSxRQUFRLENBQUM7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ3RCeEIseUVBQTBCO0FBQzFCLHlGQUF1QztBQUN2QywwRkFLcUI7QUFDckIscUdBQWtFO0FBQ2xFLGdGQUFtQztBQUNuQyxtRkFBaUU7QUFDakUsK0ZBQStDO0FBUy9DO0lBQXFDLDJCQUdwQztJQUtHLGlCQUFZLEtBQUs7UUFBakIsWUFDSSxrQkFBTSxLQUFLLENBQUMsU0F5QmY7UUF4QkcsS0FBSSxDQUFDLEtBQUssR0FBRztZQUNULE1BQU0sRUFBRSxJQUFJO1lBQ1osS0FBSyxFQUFFLEtBQUs7WUFDWixJQUFJLEVBQUUsSUFBSTtZQUNWLFFBQVEsRUFBRSxFQUFFO1lBQ1osUUFB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LE1BQU0sQ0FBQyxDQUFDO0lBQ3ZDLENBQUM7Q0FDSixDQUFDO0FBRUssSUFBTSxnQkFBZ0IsR0FBRyxVQUM1QixTQUFpQixFQUNqQixLQUFVLEVBQ1YsSUFBUyxFQUNULElBQWdCLEVBQ2hCLFNBQWlDO0lBRWpDLElBQU0sQ0FBQyxHQUFHLFVBQVUsQ0FBQyxTQUFTLENBQUMsQ0FBQztJQUNoQyxJQUFNLFFBQVEsR0FBRyxDQUFDLENBQUMsS0FBSyxFQUFFLElBQUksRUFBRSxTQUFTLENBQUMsQ0FBQztJQUMzQyxJQUFJLElBQUksQ0FBQyxNQUFNLEVBQUU7UUFDYixJQUFNLENBQUMsR0FBRyxJQUFJLENBQUMsQ0FBQyxDQUFDLENBQUM7UUFDbEIsT0FBTyx3QkFBZ0IsQ0FDbkIsQ0FBQyxDQUFDLFNBQVMsRUFDWCxRQUFRLEVBQ1IsQ0FBQyxDQUFDLElBQUk7UUFDTiw4Q0FBOEM7UUFDOUMsY0FBTSxDQUFDLENBQUMsQ0FBQyxJQUFJLEVBQUUsWUFBSSxDQUFDLENBQUMsRUFBRSxJQUFJLENBQUMsQ0FBQyxFQUM3QixTQUFTLENBQ1osQ0FBQztLQUNMO0lBQ0QsT0FBTyxRQUFRLENBQUM7QUFDcEIsQ0FBQyxDQUFDO0FBckJXLHdCQUFnQixvQkFxQjNCO0FBRUYsa0JBQWUsVUFBVSxDQUFDOzs7Ozs7Ozs7OztBQ3BXMUI7Ozs7Ozs7Ozs7QUNBQSIsInNvdXJjZXMiOlsid2VicGFjazovLy8vd2VicGFjay91bml2ZXJzYWxNb2R1bGVEZWZpbml0aW9uPyIsIndlYnBhY2s6Ly8vLy4vc3JjL3JlbmRlcmVyL2pzL2NvbXBvbmVudHMvUmVuZGVyZXIudHN4PyIsIndlYnBhY2s6Ly8vLy4vc3JjL3JlbmRlcmVyL2pzL2NvbXBvbmVudHMvVXBkYXRlci50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvcmVuZGVyZXIvanMvY29tcG9uZW50cy9XcmFwcGVyLnRzeD8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9yZW5kZXJlci9qcy9oeWRyYXRvci50c3g/Iiwid2VicGFjazovLy8vLi9zcmMvcmVuZGVyZXIvanMvaW5kZXgudHN4PyIsIndlYnBhY2s6Ly8vLy4vc3JjL3JlbmRlcmVyL2pzL3JlcXVlc3RzLnRzPyIsIndlYnBhY2s6Ly8vLy4vc3JjL3JlbmRlcmVyL2pzL3JlcXVpcmVtZW50cy50cz8iLCJ3ZWJwYWNrOi8vLy8uL3NyYy9yZW5kZXJlci9qcy90cmFuc2Zvcm1zLnRzPyIsIndlYnBhY2s6Ly8vL2V4dGVybmFsIHtcImNvbW1vbmpzXCI6XCJyZWFjdFwiLFwiY29tbW9uanMyXCI6XCJyZWFjdFwiLFwiYW1kXCI6XCJyZWFjdFwiLFwidW1kXCI6XCJyZWFjdFwiLFwicm9vdFwiOlwiUmVhY3RcIn0/Iiwid2VicGFjazovLy8vZXh0ZXJuYWwge1wiY29tbW9uanNcIjpcInJlYWN0LWRvbVwiLFwiY29tbW9uanMyXCI6XCJyZWFjdC1kb21cIixcImFtZFwiOlwicmVhY3QtZG9tXCIsXCJ1bWRcIjpcInJlYWN0LWRvbVwiLFwicm9vdFwiOlwiUmVhY3RET01cIn0/Il0sInNvdXJjZXNDb250ZW50IjpbIihmdW5jdGlvbiB3ZWJwYWNrVW5pdmVyc2FsTW9kdWxlRGVmaW5pdGlvbihyb290LCBmYWN0b3J5KSB7XG5cdGlmKHR5cGVvZiBleHBvcnRzID09PSAnb2JqZWN0JyAmJiB0eXBlb2YgbW9kdWxlID09PSAnb2JqZWN0Jylcblx0XHRtb2R1bGUuZXhwb3J0cyA9IGZhY3RvcnkocmVxdWlyZShcInJlYWN0XCIpLCByZXF1aXJlKFwicmVhY3QtZG9tXCIpKTtcblx0ZWxzZSBpZih0eXBlb2YgZGVmaW5lID09PSAnZnVuY3Rpb24nICYmIGRlZmluZS5hbWQpXG5cdFx0ZGVmaW5lKFtcInJlYWN0XCIsIFwicmVhY3QtZG9tXCJdLCBmYWN0b3J5KTtcblx0ZWxzZSBpZih0eXBlb2YgZXhwb3J0cyA9PT0gJ29iamVjdCcpXG5cdFx0ZXhwb3J0c1tcImRhenpsZXJfcmVuZGVyZXJcIl0gPSBmYWN0b3J5KHJlcXVpcmUoXCJyZWFjdFwiKSwgcmVxdWlyZShcInJlYWN0LWRvbVwiKSk7XG5cdGVsc2Vcblx0XHRyb290W1wiZGF6emxlcl9yZW5kZXJlclwiXSA9IGZhY3Rvcnkocm9vdFtcIlJlYWN0XCJdLCByb290W1wiUmVhY3RET01cIl0pO1xufSkoc2VsZiwgZnVuY3Rpb24oX19XRUJQQUNLX0VYVEVSTkFMX01PRFVMRV9yZWFjdF9fLCBfX1dFQlBBQ0tfRVhURVJOQUxfTU9EVUxFX3JlYWN0X2RvbV9fKSB7XG5yZXR1cm4gIiwiaW1wb3J0IFJlYWN0LCB7dXNlU3RhdGV9IGZyb20gJ3JlYWN0JztcbmltcG9ydCBVcGRhdGVyIGZyb20gJy4vVXBkYXRlcic7XG5cbmltcG9ydCB7UmVuZGVyT3B0aW9uc30gZnJvbSAnLi4vdHlwZXMnO1xuXG5jb25zdCBSZW5kZXJlciA9IChwcm9wczogUmVuZGVyT3B0aW9ucykgPT4ge1xuICAgIGNvbnN0IFtyZWxvYWRLZXksIHNldFJlbG9hZEtleV0gPSB1c2VTdGF0ZSgxKTtcblxuICAgIC8vIEZJWE1FIGZpbmQgd2hlcmUgdGhpcyBpcyB1c2VkIGFuZCByZWZhY3Rvci9yZW1vdmVcbiAgICAvLyBAdHMtaWdub3JlXG4gICAgd2luZG93LmRhenpsZXJfYmFzZV91cmwgPSBwcm9wcy5iYXNlVXJsO1xuICAgIHJldHVybiAoXG4gICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiZGF6emxlci1yZW5kZXJlclwiPlxuICAgICAgICAgICAgPFVwZGF0ZXJcbiAgICAgICAgICAgICAgICB7Li4ucHJvcHN9XG4gICAgICAgICAgICAgICAga2V5PXtgdXBkLSR7cmVsb2FkS2V5fWB9XG4gICAgICAgICAgICAgICAgaG90UmVsb2FkPXsoKSA9PiBzZXRSZWxvYWRLZXkocmVsb2FkS2V5ICsgMSl9XG4gICAgICAgICAgICAvPlxuICAgICAgICA8L2Rpdj5cbiAgICApO1xufTtcblxuZXhwb3J0IGRlZmF1bHQgUmVuZGVyZXI7XG4iLCJpbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHthcGlSZXF1ZXN0fSBmcm9tICcuLi9yZXF1ZXN0cyc7XG5pbXBvcnQge1xuICAgIGh5ZHJhdGVDb21wb25lbnQsXG4gICAgaHlkcmF0ZVByb3BzLFxuICAgIGlzQ29tcG9uZW50LFxuICAgIHByZXBhcmVQcm9wLFxufSBmcm9tICcuLi9oeWRyYXRvcic7XG5pbXBvcnQge2xvYWRSZXF1aXJlbWVudCwgbG9hZFJlcXVpcmVtZW50c30gZnJvbSAnLi4vcmVxdWlyZW1lbnRzJztcbmltcG9ydCB7ZGlzYWJsZUNzc30gZnJvbSAnY29tbW9ucyc7XG5pbXBvcnQge3BpY2tCeSwga2V5cywgbWFwLCBldm9sdmUsIGNvbmNhdCwgZmxhdHRlbn0gZnJvbSAncmFtZGEnO1xuaW1wb3J0IHtleGVjdXRlVHJhbnNmb3JtfSBmcm9tICcuLi90cmFuc2Zvcm1zJztcbmltcG9ydCB7XG4gICAgQmluZGluZyxcbiAgICBCb3VuZENvbXBvbmVudHMsXG4gICAgRXZvbHZlZEJpbmRpbmcsXG4gICAgVXBkYXRlclByb3BzLFxuICAgIFVwZGF0ZXJTdGF0ZSxcbn0gZnJvbSAnLi4vdHlwZXMnO1xuXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBVcGRhdGVyIGV4dGVuZHMgUmVhY3QuQ29tcG9uZW50PFxuICAgIFVwZGF0ZXJQcm9wcyxcbiAgICBVcGRhdGVyU3RhdGVcbj4ge1xuICAgIHByaXZhdGUgcGFnZUFwaTogRnVuY3Rpb247XG4gICAgcHJpdmF0ZSByZWFkb25seSBib3VuZENvbXBvbmVudHM6IEJvdW5kQ29tcG9uZW50cztcbiAgICBwcml2YXRlIHdzOiBXZWJTb2NrZXQ7XG5cbiAgICBjb25zdHJ1Y3Rvcihwcm9wcykge1xuICAgICAgICBzdXBlcihwcm9wcyk7XG4gICAgICAgIHRoaXMuc3RhdGUgPSB7XG4gICAgICAgICAgICBsYXlvdXQ6IG51bGwsXG4gICAgICAgICAgICByZWFkeTogZmFsc2UsXG4gICAgICAgICAgICBwYWdlOiBudWxsLFxuICAgICAgICAgICAgYmluZGluZ3M6IHt9LFxuICAgICAgICAgICAgcGFja2FnZXM6IFtdLFxuICAgICAgICAgICAgcmVsb2FkOiBmYWxzZSxcbiAgICAgICAgICAgIHJlYmluZGluZ3M6IFtdLFxuICAgICAgICAgICAgcmVxdWlyZW1lbnRzOiBbXSxcbiAgICAgICAgICAgIHJlbG9hZGluZzogZmFsc2UsXG4gICAgICAgICAgICBuZWVkUmVmcmVzaDogZmFsc2UsXG4gICAgICAgICAgICB0aWVzOiB7fSxcbiAgICAgICAgfTtcbiAgICAgICAgLy8gVGhlIGFwaSB1cmwgZm9yIHRoZSBwYWdlIGlzIHRoZSBzYW1lIGJ1dCBhIHBvc3QuXG4gICAgICAgIC8vIEZldGNoIGJpbmRpbmdzLCBwYWNrYWdlcyAmIHJlcXVpcmVtZW50c1xuICAgICAgICB0aGlzLnBhZ2VBcGkgPSBhcGlSZXF1ZXN0KHdpbmRvdy5sb2NhdGlvbi5ocmVmKTtcbiAgICAgICAgLy8gQWxsIGNvbXBvbmVudHMgZ2V0IGNvbm5lY3RlZC5cbiAgICAgICAgdGhpcy5ib3VuZENvbXBvbmVudHMgPSB7fTtcbiAgICAgICAgdGhpcy53cyA9IG51bGw7XG5cbiAgICAgICAgdGhpcy51cGRhdGVBc3BlY3RzID0gdGhpcy51cGRhdGVBc3BlY3RzLmJpbmQodGhpcyk7XG4gICAgICAgIHRoaXMuY29ubmVjdCA9IHRoaXMuY29ubmVjdC5iaW5kKHRoaXMpO1xuICAgICAgICB0aGlzLmRpc2Nvbm5lY3QgPSB0aGlzLmRpc2Nvbm5lY3QuYmluZCh0aGlzKTtcbiAgICAgICAgdGhpcy5vbk1lc3NhZ2UgPSB0aGlzLm9uTWVzc2FnZS5iaW5kKHRoaXMpO1xuICAgIH1cblxuICAgIHVwZGF0ZUFzcGVjdHMoaWRlbnRpdHksIGFzcGVjdHMpIHtcbiAgICAgICAgcmV0dXJuIG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7XG4gICAgICAgICAgICBjb25zdCBhc3BlY3RLZXlzID0ga2V5cyhhc3BlY3RzKTtcbiAgICAgICAgICAgIGxldCBiaW5kaW5nczogQmluZGluZ1tdIHwgRXZvbHZlZEJpbmRpbmdbXSA9IGFzcGVjdEtleXNcbiAgICAgICAgICAgICAgICAubWFwKChrZXk6IHN0cmluZykgPT4gKHtcbiAgICAgICAgICAgICAgICAgICAgLi4udGhpcy5zdGF0ZS5iaW5kaW5nc1tgJHtrZXl9QCR7aWRlbnRpdHl9YF0sXG4gICAgICAgICAgICAgICAgICAgIHZhbHVlOiBhc3BlY3RzW2tleV0sXG4gICAgICAgICAgICAgICAgfSkpXG4gICAgICAgICAgICAgICAgLmZpbHRlcigoZSkgPT4gZS50cmlnZ2VyKTtcblxuICAgICAgICAgICAgdGhpcy5zdGF0ZS5yZWJpbmRpbmdzLmZvckVhY2goKGJpbmRpbmcpID0+IHtcbiAgICAgICAgICAgICAgICBpZiAoYmluZGluZy50cmlnZ2VyLmlkZW50aXR5LnRlc3QoaWRlbnRpdHkpKSB7XG4gICAgICAgICAgICAgICAgICAgIC8vIEB0cy1pZ25vcmVcbiAgICAgICAgICAgICAgICAgICAgYmluZGluZ3MgPSBjb25jYXQoXG4gICAgICAgICAgICAgICAgICAgICAgICBiaW5kaW5ncyxcbiAgICAgICAgICAgICAgICAgICAgICAgIGFzcGVjdEtleXNcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAuZmlsdGVyKChrOiBzdHJpbmcpID0+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJpbmRpbmcudHJpZ2dlci5hc3BlY3QudGVzdChrKVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAubWFwKChrKSA9PiAoe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAuLi5iaW5kaW5nLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB2YWx1ZTogYXNwZWN0c1trXSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJpZ2dlcjoge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLi4uYmluZGluZy50cmlnZ2VyLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWRlbnRpdHksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhc3BlY3Q6IGssXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSkpXG4gICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfSk7XG5cbiAgICAgICAgICAgIGZsYXR0ZW4oXG4gICAgICAgICAgICAgICAgYXNwZWN0S2V5cy5tYXAoKGtleSkgPT4ge1xuICAgICAgICAgICAgICAgICAgICBjb25zdCB0aWVzID0gW107XG4gICAgICAgICAgICAgICAgICAgIGZvciAobGV0IGkgPSAwOyBpIDwgdGhpcy5zdGF0ZS50aWVzLmxlbmd0aDsgaSsrKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICBjb25zdCB0aWUgPSB0aGlzLnN0YXRlLnRpZXNbaV07XG4gICAgICAgICAgICAgICAgICAgICAgICBjb25zdCB7dHJpZ2dlcn0gPSB0aWU7XG4gICAgICAgICAgICAgICAgICAgICAgICBpZiAoXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgKHRyaWdnZXIucmVnZXggJiZcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJpZ2dlci5pZGVudGl0eS50ZXN0KGlkZW50aXR5KSAmJlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cmlnZ2VyLmFzcGVjdC50ZXN0KGtleSkpIHx8XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgKHRyaWdnZXIuaWRlbnRpdHkgPT09IGlkZW50aXR5ICYmXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRyaWdnZXIuYXNwZWN0ID09PSBrZXkpXG4gICAgICAgICAgICAgICAgICAgICAgICApIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aWVzLnB1c2goe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAuLi50aWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhbHVlOiBhc3BlY3RzW2tleV0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIHRpZXM7XG4gICAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgICkuZm9yRWFjaCgodGllKSA9PiB7XG4gICAgICAgICAgICAgICAgY29uc3Qge3RyYW5zZm9ybXN9ID0gdGllO1xuICAgICAgICAgICAgICAgIGxldCB2YWx1ZSA9IHRpZS52YWx1ZTtcbiAgICAgICAgICAgICAgICBpZiAodHJhbnNmb3Jtcykge1xuICAgICAgICAgICAgICAgICAgICB2YWx1ZSA9IHRyYW5zZm9ybXMucmVkdWNlKChhY2MsIGUpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybiBleGVjdXRlVHJhbnNmb3JtKFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGUudHJhbnNmb3JtLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFjYyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBlLmFyZ3MsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgZS5uZXh0LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRoaXMuZ2V0QXNwZWN0LmJpbmQodGhpcylcbiAgICAgICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgIH0sIHZhbHVlKTtcbiAgICAgICAgICAgICAgICB9XG5cbiAgICAgICAgICAgICAgICB0aWUudGFyZ2V0cy5mb3JFYWNoKCh0KSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIGNvbnN0IGNvbXBvbmVudCA9IHRoaXMuYm91bmRDb21wb25lbnRzW3QuaWRlbnRpdHldO1xuICAgICAgICAgICAgICAgICAgICBpZiAoY29tcG9uZW50KSB7XG4gICAgICAgICAgICAgICAgICAgICAgICBjb21wb25lbnQudXBkYXRlQXNwZWN0cyh7W3QuYXNwZWN0XTogdmFsdWV9KTtcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfSk7XG5cbiAgICAgICAgICAgIGlmICghYmluZGluZ3MpIHtcbiAgICAgICAgICAgICAgICByZXNvbHZlKDApO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICBiaW5kaW5ncy5mb3JFYWNoKChiaW5kaW5nKSA9PlxuICAgICAgICAgICAgICAgICAgICB0aGlzLnNlbmRCaW5kaW5nKGJpbmRpbmcsIGJpbmRpbmcudmFsdWUpXG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICByZXNvbHZlKGJpbmRpbmdzLmxlbmd0aCk7XG4gICAgICAgICAgICB9XG4gICAgICAgIH0pO1xuICAgIH1cblxuICAgIGdldEFzcGVjdChpZGVudGl0eSwgYXNwZWN0KTogYW55IHwgdW5kZWZpbmVkIHtcbiAgICAgICAgY29uc3QgYyA9IHRoaXMuYm91bmRDb21wb25lbnRzW2lkZW50aXR5XTtcbiAgICAgICAgaWYgKGMpIHtcbiAgICAgICAgICAgIHJldHVybiBjLmdldEFzcGVjdChhc3BlY3QpO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB1bmRlZmluZWQ7XG4gICAgfVxuXG4gICAgY29ubmVjdChpZGVudGl0eSwgc2V0QXNwZWN0cywgZ2V0QXNwZWN0LCBtYXRjaEFzcGVjdHMsIHVwZGF0ZUFzcGVjdHMpIHtcbiAgICAgICAgdGhpcy5ib3VuZENvbXBvbmVudHNbaWRlbnRpdHldID0ge1xuICAgICAgICAgICAgc2V0QXNwZWN0cyxcbiAgICAgICAgICAgIGdldEFzcGVjdCxcbiAgICAgICAgICAgIG1hdGNoQXNwZWN0cyxcbiAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgICAgIH07XG4gICAgfVxuXG4gICAgZGlzY29ubmVjdChpZGVudGl0eSkge1xuICAgICAgICBkZWxldGUgdGhpcy5ib3VuZENvbXBvbmVudHNbaWRlbnRpdHldO1xuICAgIH1cblxuICAgIG9uTWVzc2FnZShyZXNwb25zZSkge1xuICAgICAgICBjb25zdCBkYXRhID0gSlNPTi5wYXJzZShyZXNwb25zZS5kYXRhKTtcbiAgICAgICAgY29uc3Qge2lkZW50aXR5LCBraW5kLCBwYXlsb2FkLCBzdG9yYWdlLCByZXF1ZXN0X2lkfSA9IGRhdGE7XG4gICAgICAgIGxldCBzdG9yZTtcbiAgICAgICAgaWYgKHN0b3JhZ2UgPT09ICdzZXNzaW9uJykge1xuICAgICAgICAgICAgc3RvcmUgPSB3aW5kb3cuc2Vzc2lvblN0b3JhZ2U7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICBzdG9yZSA9IHdpbmRvdy5sb2NhbFN0b3JhZ2U7XG4gICAgICAgIH1cbiAgICAgICAgc3dpdGNoIChraW5kKSB7XG4gICAgICAgICAgICBjYXNlICdzZXQtYXNwZWN0JzpcbiAgICAgICAgICAgICAgICBjb25zdCBzZXRBc3BlY3RzID0gKGNvbXBvbmVudCkgPT5cbiAgICAgICAgICAgICAgICAgICAgY29tcG9uZW50XG4gICAgICAgICAgICAgICAgICAgICAgICAuc2V0QXNwZWN0cyhcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBoeWRyYXRlUHJvcHMoXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBheWxvYWQsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRoaXMudXBkYXRlQXNwZWN0cyxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGhpcy5jb25uZWN0LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aGlzLmRpc2Nvbm5lY3RcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgICAgICAgICAudGhlbigoKSA9PiB0aGlzLnVwZGF0ZUFzcGVjdHMoaWRlbnRpdHksIHBheWxvYWQpKTtcbiAgICAgICAgICAgICAgICBpZiAoZGF0YS5yZWdleCkge1xuICAgICAgICAgICAgICAgICAgICBjb25zdCBwYXR0ZXJuID0gbmV3IFJlZ0V4cChkYXRhLmlkZW50aXR5KTtcbiAgICAgICAgICAgICAgICAgICAga2V5cyh0aGlzLmJvdW5kQ29tcG9uZW50cylcbiAgICAgICAgICAgICAgICAgICAgICAgIC5maWx0ZXIoKGs6IHN0cmluZykgPT4gcGF0dGVybi50ZXN0KGspKVxuICAgICAgICAgICAgICAgICAgICAgICAgLm1hcCgoaykgPT4gdGhpcy5ib3VuZENvbXBvbmVudHNba10pXG4gICAgICAgICAgICAgICAgICAgICAgICAuZm9yRWFjaChzZXRBc3BlY3RzKTtcbiAgICAgICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgICAgICBzZXRBc3BlY3RzKHRoaXMuYm91bmRDb21wb25lbnRzW2lkZW50aXR5XSk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgICAgY2FzZSAnZ2V0LWFzcGVjdCc6XG4gICAgICAgICAgICAgICAgY29uc3Qge2FzcGVjdH0gPSBkYXRhO1xuICAgICAgICAgICAgICAgIGNvbnN0IHdhbnRlZCA9IHRoaXMuYm91bmRDb21wb25lbnRzW2lkZW50aXR5XTtcbiAgICAgICAgICAgICAgICBpZiAoIXdhbnRlZCkge1xuICAgICAgICAgICAgICAgICAgICB0aGlzLndzLnNlbmQoXG4gICAgICAgICAgICAgICAgICAgICAgICBKU09OLnN0cmluZ2lmeSh7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAga2luZCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZGVudGl0eSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhc3BlY3QsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcmVxdWVzdF9pZCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBlcnJvcjogYEFzcGVjdCBub3QgZm91bmQgJHtpZGVudGl0eX0uJHthc3BlY3R9YCxcbiAgICAgICAgICAgICAgICAgICAgICAgIH0pXG4gICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgY29uc3QgdmFsdWUgPSB3YW50ZWQuZ2V0QXNwZWN0KGFzcGVjdCk7XG4gICAgICAgICAgICAgICAgdGhpcy53cy5zZW5kKFxuICAgICAgICAgICAgICAgICAgICBKU09OLnN0cmluZ2lmeSh7XG4gICAgICAgICAgICAgICAgICAgICAgICBraW5kLFxuICAgICAgICAgICAgICAgICAgICAgICAgaWRlbnRpdHksXG4gICAgICAgICAgICAgICAgICAgICAgICBhc3BlY3QsXG4gICAgICAgICAgICAgICAgICAgICAgICB2YWx1ZTogcHJlcGFyZVByb3AodmFsdWUpLFxuICAgICAgICAgICAgICAgICAgICAgICAgcmVxdWVzdF9pZCxcbiAgICAgICAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgICAgY2FzZSAnc2V0LXN0b3JhZ2UnOlxuICAgICAgICAgICAgICAgIHN0b3JlLnNldEl0ZW0oaWRlbnRpdHksIEpTT04uc3RyaW5naWZ5KHBheWxvYWQpKTtcbiAgICAgICAgICAgICAgICBicmVhaztcbiAgICAgICAgICAgIGNhc2UgJ2dldC1zdG9yYWdlJzpcbiAgICAgICAgICAgICAgICB0aGlzLndzLnNlbmQoXG4gICAgICAgICAgICAgICAgICAgIEpTT04uc3RyaW5naWZ5KHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGtpbmQsXG4gICAgICAgICAgICAgICAgICAgICAgICBpZGVudGl0eSxcbiAgICAgICAgICAgICAgICAgICAgICAgIHJlcXVlc3RfaWQsXG4gICAgICAgICAgICAgICAgICAgICAgICB2YWx1ZTogSlNPTi5wYXJzZShzdG9yZS5nZXRJdGVtKGlkZW50aXR5KSksXG4gICAgICAgICAgICAgICAgICAgIH0pXG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICBicmVhaztcbiAgICAgICAgICAgIGNhc2UgJ3JlbG9hZCc6XG4gICAgICAgICAgICAgICAgY29uc3Qge2ZpbGVuYW1lcywgaG90LCByZWZyZXNoLCBkZWxldGVkfSA9IGRhdGE7XG4gICAgICAgICAgICAgICAgaWYgKHJlZnJlc2gpIHtcbiAgICAgICAgICAgICAgICAgICAgdGhpcy53cy5jbG9zZSgpO1xuICAgICAgICAgICAgICAgICAgICB0aGlzLnNldFN0YXRlKHtyZWxvYWRpbmc6IHRydWUsIG5lZWRSZWZyZXNoOiB0cnVlfSk7XG4gICAgICAgICAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgaWYgKGhvdCkge1xuICAgICAgICAgICAgICAgICAgICAvLyBUaGUgd3MgY29ubmVjdGlvbiB3aWxsIGNsb3NlLCB3aGVuIGl0XG4gICAgICAgICAgICAgICAgICAgIC8vIHJlY29ubmVjdCBpdCB3aWxsIGRvIGEgaGFyZCByZWxvYWQgb2YgdGhlIHBhZ2UgYXBpLlxuICAgICAgICAgICAgICAgICAgICB0aGlzLnNldFN0YXRlKHtyZWxvYWRpbmc6IHRydWV9KTtcbiAgICAgICAgICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICBmaWxlbmFtZXMuZm9yRWFjaChsb2FkUmVxdWlyZW1lbnQpO1xuICAgICAgICAgICAgICAgIGRlbGV0ZWQuZm9yRWFjaCgocikgPT4gZGlzYWJsZUNzcyhyLnVybCkpO1xuICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgICAgY2FzZSAncGluZyc6XG4gICAgICAgICAgICAgICAgLy8gSnVzdCBkbyBub3RoaW5nLlxuICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICB9XG4gICAgfVxuXG4gICAgc2VuZEJpbmRpbmcoYmluZGluZywgdmFsdWUpIHtcbiAgICAgICAgLy8gQ29sbGVjdCBhbGwgdmFsdWVzIGFuZCBzZW5kIGEgYmluZGluZyBwYXlsb2FkXG4gICAgICAgIGNvbnN0IHRyaWdnZXIgPSB7XG4gICAgICAgICAgICAuLi5iaW5kaW5nLnRyaWdnZXIsXG4gICAgICAgICAgICB2YWx1ZTogcHJlcGFyZVByb3AodmFsdWUpLFxuICAgICAgICB9O1xuICAgICAgICBjb25zdCBzdGF0ZXMgPSBiaW5kaW5nLnN0YXRlcy5yZWR1Y2UoKGFjYywgc3RhdGUpID0+IHtcbiAgICAgICAgICAgIGlmIChzdGF0ZS5yZWdleCkge1xuICAgICAgICAgICAgICAgIGNvbnN0IGlkZW50aXR5UGF0dGVybiA9IG5ldyBSZWdFeHAoc3RhdGUuaWRlbnRpdHkpO1xuICAgICAgICAgICAgICAgIGNvbnN0IGFzcGVjdFBhdHRlcm4gPSBuZXcgUmVnRXhwKHN0YXRlLmFzcGVjdCk7XG4gICAgICAgICAgICAgICAgcmV0dXJuIGNvbmNhdChcbiAgICAgICAgICAgICAgICAgICAgYWNjLFxuICAgICAgICAgICAgICAgICAgICBmbGF0dGVuKFxuICAgICAgICAgICAgICAgICAgICAgICAga2V5cyh0aGlzLmJvdW5kQ29tcG9uZW50cykubWFwKChrOiBzdHJpbmcpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsZXQgdmFsdWVzID0gW107XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgKGlkZW50aXR5UGF0dGVybi50ZXN0KGspKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhbHVlcyA9IHRoaXMuYm91bmRDb21wb25lbnRzW2tdXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAubWF0Y2hBc3BlY3RzKGFzcGVjdFBhdHRlcm4pXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAubWFwKChbbmFtZSwgdmFsXSkgPT4gKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAuLi5zdGF0ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZGVudGl0eTogayxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhc3BlY3Q6IG5hbWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFsdWU6IHByZXBhcmVQcm9wKHZhbCksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybiB2YWx1ZXM7XG4gICAgICAgICAgICAgICAgICAgICAgICB9KVxuICAgICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgYWNjLnB1c2goe1xuICAgICAgICAgICAgICAgIC4uLnN0YXRlLFxuICAgICAgICAgICAgICAgIHZhbHVlOlxuICAgICAgICAgICAgICAgICAgICB0aGlzLmJvdW5kQ29tcG9uZW50c1tzdGF0ZS5pZGVudGl0eV0gJiZcbiAgICAgICAgICAgICAgICAgICAgcHJlcGFyZVByb3AoXG4gICAgICAgICAgICAgICAgICAgICAgICB0aGlzLmJvdW5kQ29tcG9uZW50c1tzdGF0ZS5pZGVudGl0eV0uZ2V0QXNwZWN0KFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlLmFzcGVjdFxuICAgICAgICAgICAgICAgICAgICAgICAgKVxuICAgICAgICAgICAgICAgICAgICApLFxuICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICByZXR1cm4gYWNjO1xuICAgICAgICB9LCBbXSk7XG5cbiAgICAgICAgY29uc3QgcGF5bG9hZCA9IHtcbiAgICAgICAgICAgIHRyaWdnZXIsXG4gICAgICAgICAgICBzdGF0ZXMsXG4gICAgICAgICAgICBraW5kOiAnYmluZGluZycsXG4gICAgICAgICAgICBwYWdlOiB0aGlzLnN0YXRlLnBhZ2UsXG4gICAgICAgICAgICBrZXk6IGJpbmRpbmcua2V5LFxuICAgICAgICB9O1xuICAgICAgICB0aGlzLndzLnNlbmQoSlNPTi5zdHJpbmdpZnkocGF5bG9hZCkpO1xuICAgIH1cblxuICAgIF9jb25uZWN0V1MoKSB7XG4gICAgICAgIC8vIFNldHVwIHdlYnNvY2tldCBmb3IgdXBkYXRlc1xuICAgICAgICBsZXQgdHJpZXMgPSAwO1xuICAgICAgICBsZXQgaGFyZENsb3NlID0gZmFsc2U7XG4gICAgICAgIGNvbnN0IGNvbm5leGlvbiA9ICgpID0+IHtcbiAgICAgICAgICAgIGNvbnN0IHVybCA9IGB3cyR7XG4gICAgICAgICAgICAgICAgd2luZG93LmxvY2F0aW9uLmhyZWYuc3RhcnRzV2l0aCgnaHR0cHMnKSA/ICdzJyA6ICcnXG4gICAgICAgICAgICB9Oi8vJHtcbiAgICAgICAgICAgICAgICAodGhpcy5wcm9wcy5iYXNlVXJsICYmIHRoaXMucHJvcHMuYmFzZVVybCkgfHxcbiAgICAgICAgICAgICAgICB3aW5kb3cubG9jYXRpb24uaG9zdFxuICAgICAgICAgICAgfS8ke3RoaXMuc3RhdGUucGFnZX0vd3NgO1xuICAgICAgICAgICAgdGhpcy53cyA9IG5ldyBXZWJTb2NrZXQodXJsKTtcbiAgICAgICAgICAgIHRoaXMud3MuYWRkRXZlbnRMaXN0ZW5lcignbWVzc2FnZScsIHRoaXMub25NZXNzYWdlKTtcbiAgICAgICAgICAgIHRoaXMud3Mub25vcGVuID0gKCkgPT4ge1xuICAgICAgICAgICAgICAgIGlmICh0aGlzLnN0YXRlLnJlbG9hZGluZykge1xuICAgICAgICAgICAgICAgICAgICBoYXJkQ2xvc2UgPSB0cnVlO1xuICAgICAgICAgICAgICAgICAgICB0aGlzLndzLmNsb3NlKCk7XG4gICAgICAgICAgICAgICAgICAgIGlmICh0aGlzLnN0YXRlLm5lZWRSZWZyZXNoKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cubG9jYXRpb24ucmVsb2FkKCk7XG4gICAgICAgICAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgICAgICAgICB0aGlzLnByb3BzLmhvdFJlbG9hZCgpO1xuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICAgICAgdGhpcy5zZXRTdGF0ZSh7cmVhZHk6IHRydWV9KTtcbiAgICAgICAgICAgICAgICAgICAgdHJpZXMgPSAwO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH07XG4gICAgICAgICAgICB0aGlzLndzLm9uY2xvc2UgPSAoKSA9PiB7XG4gICAgICAgICAgICAgICAgY29uc3QgcmVjb25uZWN0ID0gKCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICB0cmllcysrO1xuICAgICAgICAgICAgICAgICAgICBjb25uZXhpb24oKTtcbiAgICAgICAgICAgICAgICB9O1xuICAgICAgICAgICAgICAgIGlmICghaGFyZENsb3NlICYmIHRyaWVzIDwgdGhpcy5wcm9wcy5yZXRyaWVzKSB7XG4gICAgICAgICAgICAgICAgICAgIHNldFRpbWVvdXQocmVjb25uZWN0LCAxMDAwKTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9O1xuICAgICAgICB9O1xuICAgICAgICBjb25uZXhpb24oKTtcbiAgICB9XG5cbiAgICBjb21wb25lbnREaWRNb3VudCgpIHtcbiAgICAgICAgdGhpcy5wYWdlQXBpKCcnLCB7bWV0aG9kOiAnUE9TVCd9KS50aGVuKChyZXNwb25zZSkgPT4ge1xuICAgICAgICAgICAgY29uc3QgdG9SZWdleCA9ICh4KSA9PiBuZXcgUmVnRXhwKHgpO1xuICAgICAgICAgICAgdGhpcy5zZXRTdGF0ZShcbiAgICAgICAgICAgICAgICB7XG4gICAgICAgICAgICAgICAgICAgIHBhZ2U6IHJlc3BvbnNlLnBhZ2UsXG4gICAgICAgICAgICAgICAgICAgIGxheW91dDogcmVzcG9uc2UubGF5b3V0LFxuICAgICAgICAgICAgICAgICAgICBiaW5kaW5nczogcGlja0J5KChiKSA9PiAhYi5yZWdleCwgcmVzcG9uc2UuYmluZGluZ3MpLFxuICAgICAgICAgICAgICAgICAgICAvLyBSZWdleCBiaW5kaW5ncyB0cmlnZ2Vyc1xuICAgICAgICAgICAgICAgICAgICByZWJpbmRpbmdzOiBtYXAoKHgpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGNvbnN0IGJpbmRpbmcgPSByZXNwb25zZS5iaW5kaW5nc1t4XTtcbiAgICAgICAgICAgICAgICAgICAgICAgIGJpbmRpbmcudHJpZ2dlciA9IGV2b2x2ZShcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlkZW50aXR5OiB0b1JlZ2V4LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhc3BlY3Q6IHRvUmVnZXgsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBiaW5kaW5nLnRyaWdnZXJcbiAgICAgICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gYmluZGluZztcbiAgICAgICAgICAgICAgICAgICAgfSwga2V5cyhwaWNrQnkoKGIpID0+IGIucmVnZXgsIHJlc3BvbnNlLmJpbmRpbmdzKSkpLFxuICAgICAgICAgICAgICAgICAgICBwYWNrYWdlczogcmVzcG9uc2UucGFja2FnZXMsXG4gICAgICAgICAgICAgICAgICAgIHJlcXVpcmVtZW50czogcmVzcG9uc2UucmVxdWlyZW1lbnRzLFxuICAgICAgICAgICAgICAgICAgICB0aWVzOiBtYXAoKHRpZSkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKHRpZS50cmlnZ2VyLnJlZ2V4KSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcmV0dXJuIGV2b2x2ZShcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJpZ2dlcjoge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlkZW50aXR5OiB0b1JlZ2V4LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFzcGVjdDogdG9SZWdleCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gdGllO1xuICAgICAgICAgICAgICAgICAgICB9LCByZXNwb25zZS50aWVzKSxcbiAgICAgICAgICAgICAgICB9LFxuICAgICAgICAgICAgICAgICgpID0+XG4gICAgICAgICAgICAgICAgICAgIGxvYWRSZXF1aXJlbWVudHMoXG4gICAgICAgICAgICAgICAgICAgICAgICByZXNwb25zZS5yZXF1aXJlbWVudHMsXG4gICAgICAgICAgICAgICAgICAgICAgICByZXNwb25zZS5wYWNrYWdlc1xuICAgICAgICAgICAgICAgICAgICApLnRoZW4oKCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKGtleXMocmVzcG9uc2UuYmluZGluZ3MpLmxlbmd0aCB8fCByZXNwb25zZS5yZWxvYWQpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aGlzLl9jb25uZWN0V1MoKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdGhpcy5zZXRTdGF0ZSh7cmVhZHk6IHRydWV9KTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgICk7XG4gICAgICAgIH0pO1xuICAgIH1cblxuICAgIHJlbmRlcigpIHtcbiAgICAgICAgY29uc3Qge2xheW91dCwgcmVhZHksIHJlbG9hZGluZ30gPSB0aGlzLnN0YXRlO1xuICAgICAgICBpZiAoIXJlYWR5KSB7XG4gICAgICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiZGF6emxlci1sb2FkaW5nLWNvbnRhaW5lclwiPlxuICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImRhenpsZXItc3BpblwiIC8+XG4gICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiZGF6emxlci1sb2FkaW5nXCI+TG9hZGluZy4uLjwvZGl2PlxuICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgICAgICBpZiAocmVsb2FkaW5nKSB7XG4gICAgICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiZGF6emxlci1sb2FkaW5nLWNvbnRhaW5lclwiPlxuICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImRhenpsZXItc3BpbiByZWxvYWRcIiAvPlxuICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImRhenpsZXItbG9hZGluZ1wiPlJlbG9hZGluZy4uLjwvZGl2PlxuICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgICAgICBpZiAoIWlzQ29tcG9uZW50KGxheW91dCkpIHtcbiAgICAgICAgICAgIHRocm93IG5ldyBFcnJvcihgTGF5b3V0IGlzIG5vdCBhIGNvbXBvbmVudDogJHtsYXlvdXR9YCk7XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCBjb250ZXh0cyA9IFtdO1xuXG4gICAgICAgIGNvbnN0IG9uQ29udGV4dCA9IChjb250ZXh0Q29tcG9uZW50KSA9PiB7XG4gICAgICAgICAgICBjb250ZXh0cy5wdXNoKGNvbnRleHRDb21wb25lbnQpO1xuICAgICAgICB9O1xuXG4gICAgICAgIGNvbnN0IGh5ZHJhdGVkID0gaHlkcmF0ZUNvbXBvbmVudChcbiAgICAgICAgICAgIGxheW91dC5uYW1lLFxuICAgICAgICAgICAgbGF5b3V0LnBhY2thZ2UsXG4gICAgICAgICAgICBsYXlvdXQuaWRlbnRpdHksXG4gICAgICAgICAgICBoeWRyYXRlUHJvcHMoXG4gICAgICAgICAgICAgICAgbGF5b3V0LmFzcGVjdHMsXG4gICAgICAgICAgICAgICAgdGhpcy51cGRhdGVBc3BlY3RzLFxuICAgICAgICAgICAgICAgIHRoaXMuY29ubmVjdCxcbiAgICAgICAgICAgICAgICB0aGlzLmRpc2Nvbm5lY3QsXG4gICAgICAgICAgICAgICAgb25Db250ZXh0XG4gICAgICAgICAgICApLFxuICAgICAgICAgICAgdGhpcy51cGRhdGVBc3BlY3RzLFxuICAgICAgICAgICAgdGhpcy5jb25uZWN0LFxuICAgICAgICAgICAgdGhpcy5kaXNjb25uZWN0LFxuICAgICAgICAgICAgb25Db250ZXh0XG4gICAgICAgICk7XG5cbiAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiZGF6emxlci1yZW5kZXJlZFwiPlxuICAgICAgICAgICAgICAgIHtjb250ZXh0cy5sZW5ndGhcbiAgICAgICAgICAgICAgICAgICAgPyBjb250ZXh0cy5yZWR1Y2UoKGFjYywgQ29udGV4dCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgICBpZiAoIWFjYykge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcmV0dXJuIDxDb250ZXh0PntoeWRyYXRlZH08L0NvbnRleHQ+O1xuICAgICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybiA8Q29udGV4dD57YWNjfTwvQ29udGV4dD47XG4gICAgICAgICAgICAgICAgICAgICAgfSwgbnVsbClcbiAgICAgICAgICAgICAgICAgICAgOiBoeWRyYXRlZH1cbiAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICApO1xuICAgIH1cbn1cbiIsImltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQge2NvbmNhdCwgam9pbiwga2V5c30gZnJvbSAncmFtZGEnO1xuaW1wb3J0IHtjYW1lbFRvU3BpbmFsfSBmcm9tICdjb21tb25zJztcbmltcG9ydCB7V3JhcHBlclByb3BzLCBXcmFwcGVyU3RhdGV9IGZyb20gJy4uL3R5cGVzJztcblxuLyoqXG4gKiBXcmFwcyBjb21wb25lbnRzIGZvciBhc3BlY3RzIHVwZGF0aW5nLlxuICovXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBXcmFwcGVyIGV4dGVuZHMgUmVhY3QuQ29tcG9uZW50PFxuICAgIFdyYXBwZXJQcm9wcyxcbiAgICBXcmFwcGVyU3RhdGVcbj4ge1xuICAgIGNvbnN0cnVjdG9yKHByb3BzKSB7XG4gICAgICAgIHN1cGVyKHByb3BzKTtcbiAgICAgICAgdGhpcy5zdGF0ZSA9IHtcbiAgICAgICAgICAgIGFzcGVjdHM6IHByb3BzLmFzcGVjdHMgfHwge30sXG4gICAgICAgICAgICByZWFkeTogZmFsc2UsXG4gICAgICAgICAgICBpbml0aWFsOiBmYWxzZSxcbiAgICAgICAgfTtcbiAgICAgICAgdGhpcy5zZXRBc3BlY3RzID0gdGhpcy5zZXRBc3BlY3RzLmJpbmQodGhpcyk7XG4gICAgICAgIHRoaXMuZ2V0QXNwZWN0ID0gdGhpcy5nZXRBc3BlY3QuYmluZCh0aGlzKTtcbiAgICAgICAgdGhpcy51cGRhdGVBc3BlY3RzID0gdGhpcy51cGRhdGVBc3BlY3RzLmJpbmQodGhpcyk7XG4gICAgICAgIHRoaXMubWF0Y2hBc3BlY3RzID0gdGhpcy5tYXRjaEFzcGVjdHMuYmluZCh0aGlzKTtcbiAgICB9XG5cbiAgICB1cGRhdGVBc3BlY3RzKGFzcGVjdHMpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMuc2V0QXNwZWN0cyhhc3BlY3RzKS50aGVuKCgpID0+XG4gICAgICAgICAgICB0aGlzLnByb3BzLnVwZGF0ZUFzcGVjdHModGhpcy5wcm9wcy5pZGVudGl0eSwgYXNwZWN0cylcbiAgICAgICAgKTtcbiAgICB9XG5cbiAgICBzZXRBc3BlY3RzKGFzcGVjdHMpIHtcbiAgICAgICAgcmV0dXJuIG5ldyBQcm9taXNlPHZvaWQ+KChyZXNvbHZlKSA9PiB7XG4gICAgICAgICAgICB0aGlzLnNldFN0YXRlKFxuICAgICAgICAgICAgICAgIHthc3BlY3RzOiB7Li4udGhpcy5zdGF0ZS5hc3BlY3RzLCAuLi5hc3BlY3RzfX0sXG4gICAgICAgICAgICAgICAgcmVzb2x2ZVxuICAgICAgICAgICAgKTtcbiAgICAgICAgfSk7XG4gICAgfVxuXG4gICAgZ2V0QXNwZWN0KGFzcGVjdCkge1xuICAgICAgICByZXR1cm4gdGhpcy5zdGF0ZS5hc3BlY3RzW2FzcGVjdF07XG4gICAgfVxuXG4gICAgbWF0Y2hBc3BlY3RzKHBhdHRlcm4pIHtcbiAgICAgICAgcmV0dXJuIGtleXModGhpcy5zdGF0ZS5hc3BlY3RzKVxuICAgICAgICAgICAgLmZpbHRlcigoaykgPT4gcGF0dGVybi50ZXN0KGspKVxuICAgICAgICAgICAgLm1hcCgoaykgPT4gW2ssIHRoaXMuc3RhdGUuYXNwZWN0c1trXV0pO1xuICAgIH1cblxuICAgIGNvbXBvbmVudERpZE1vdW50KCkge1xuICAgICAgICAvLyBPbmx5IHVwZGF0ZSB0aGUgY29tcG9uZW50IHdoZW4gbW91bnRlZC5cbiAgICAgICAgLy8gT3RoZXJ3aXNlIGdldHMgYSByYWNlIGNvbmRpdGlvbiB3aXRoIHdpbGxVbm1vdW50XG4gICAgICAgIHRoaXMucHJvcHMuY29ubmVjdChcbiAgICAgICAgICAgIHRoaXMucHJvcHMuaWRlbnRpdHksXG4gICAgICAgICAgICB0aGlzLnNldEFzcGVjdHMsXG4gICAgICAgICAgICB0aGlzLmdldEFzcGVjdCxcbiAgICAgICAgICAgIHRoaXMubWF0Y2hBc3BlY3RzLFxuICAgICAgICAgICAgdGhpcy51cGRhdGVBc3BlY3RzXG4gICAgICAgICk7XG4gICAgICAgIGlmICghdGhpcy5zdGF0ZS5pbml0aWFsKSB7XG4gICAgICAgICAgICB0aGlzLnVwZGF0ZUFzcGVjdHModGhpcy5zdGF0ZS5hc3BlY3RzKS50aGVuKCgpID0+XG4gICAgICAgICAgICAgICAgdGhpcy5zZXRTdGF0ZSh7cmVhZHk6IHRydWUsIGluaXRpYWw6IHRydWV9KVxuICAgICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgIH1cblxuICAgIGNvbXBvbmVudFdpbGxVbm1vdW50KCkge1xuICAgICAgICB0aGlzLnByb3BzLmRpc2Nvbm5lY3QodGhpcy5wcm9wcy5pZGVudGl0eSk7XG4gICAgfVxuXG4gICAgcmVuZGVyKCkge1xuICAgICAgICBjb25zdCB7Y29tcG9uZW50LCBjb21wb25lbnRfbmFtZSwgcGFja2FnZV9uYW1lfSA9IHRoaXMucHJvcHM7XG4gICAgICAgIGNvbnN0IHthc3BlY3RzLCByZWFkeX0gPSB0aGlzLnN0YXRlO1xuICAgICAgICBpZiAoIXJlYWR5KSB7XG4gICAgICAgICAgICByZXR1cm4gbnVsbDtcbiAgICAgICAgfVxuXG4gICAgICAgIHJldHVybiBSZWFjdC5jbG9uZUVsZW1lbnQoY29tcG9uZW50LCB7XG4gICAgICAgICAgICAuLi5hc3BlY3RzLFxuICAgICAgICAgICAgdXBkYXRlQXNwZWN0czogdGhpcy51cGRhdGVBc3BlY3RzLFxuICAgICAgICAgICAgaWRlbnRpdHk6IHRoaXMucHJvcHMuaWRlbnRpdHksXG4gICAgICAgICAgICBjbGFzc19uYW1lOiBqb2luKFxuICAgICAgICAgICAgICAgICcgJyxcbiAgICAgICAgICAgICAgICBjb25jYXQoXG4gICAgICAgICAgICAgICAgICAgIFtcbiAgICAgICAgICAgICAgICAgICAgICAgIGAke3BhY2thZ2VfbmFtZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC5yZXBsYWNlKCdfJywgJy0nKVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC50b0xvd2VyQ2FzZSgpfS0ke2NhbWVsVG9TcGluYWwoY29tcG9uZW50X25hbWUpfWAsXG4gICAgICAgICAgICAgICAgICAgIF0sXG4gICAgICAgICAgICAgICAgICAgIGFzcGVjdHMuY2xhc3NfbmFtZSA/IGFzcGVjdHMuY2xhc3NfbmFtZS5zcGxpdCgnICcpIDogW11cbiAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICApLFxuICAgICAgICB9KTtcbiAgICB9XG59XG4iLCJpbXBvcnQge21hcCwgb21pdCwgdHlwZX0gZnJvbSAncmFtZGEnO1xuaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCBXcmFwcGVyIGZyb20gJy4vY29tcG9uZW50cy9XcmFwcGVyJztcbmltcG9ydCB7QW55RGljdH0gZnJvbSAnY29tbW9ucy9qcy90eXBlcyc7XG5pbXBvcnQge1xuICAgIENvbm5lY3RGdW5jLFxuICAgIERpc2Nvbm5lY3RGdW5jLFxuICAgIFdyYXBwZXJQcm9wcyxcbiAgICBXcmFwcGVyVXBkYXRlQXNwZWN0RnVuYyxcbn0gZnJvbSAnLi90eXBlcyc7XG5cbmV4cG9ydCBmdW5jdGlvbiBpc0NvbXBvbmVudChjOiBhbnkpOiBib29sZWFuIHtcbiAgICByZXR1cm4gKFxuICAgICAgICB0eXBlKGMpID09PSAnT2JqZWN0JyAmJlxuICAgICAgICBjLmhhc093blByb3BlcnR5KCdwYWNrYWdlJykgJiZcbiAgICAgICAgYy5oYXNPd25Qcm9wZXJ0eSgnYXNwZWN0cycpICYmXG4gICAgICAgIGMuaGFzT3duUHJvcGVydHkoJ25hbWUnKSAmJlxuICAgICAgICBjLmhhc093blByb3BlcnR5KCdpZGVudGl0eScpXG4gICAgKTtcbn1cblxuZXhwb3J0IGZ1bmN0aW9uIGh5ZHJhdGVQcm9wcyhcbiAgICBwcm9wczogQW55RGljdCxcbiAgICB1cGRhdGVBc3BlY3RzOiBXcmFwcGVyVXBkYXRlQXNwZWN0RnVuYyxcbiAgICBjb25uZWN0OiBDb25uZWN0RnVuYyxcbiAgICBkaXNjb25uZWN0OiBEaXNjb25uZWN0RnVuYyxcbiAgICBvbkNvbnRleHQ/OiBGdW5jdGlvblxuKSB7XG4gICAgY29uc3QgcmVwbGFjZSA9IHt9O1xuICAgIE9iamVjdC5lbnRyaWVzKHByb3BzKS5mb3JFYWNoKChbaywgdl0pID0+IHtcbiAgICAgICAgaWYgKHR5cGUodikgPT09ICdBcnJheScpIHtcbiAgICAgICAgICAgIHJlcGxhY2Vba10gPSB2Lm1hcCgoYykgPT4ge1xuICAgICAgICAgICAgICAgIGlmICghaXNDb21wb25lbnQoYykpIHtcbiAgICAgICAgICAgICAgICAgICAgLy8gTWl4aW5nIGNvbXBvbmVudHMgYW5kIHByaW1pdGl2ZXNcbiAgICAgICAgICAgICAgICAgICAgaWYgKHR5cGUoYykgPT09ICdPYmplY3QnKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAvLyBOb3QgYSBjb21wb25lbnQgYnV0IG1heWJlIGl0IGNvbnRhaW5zIHNvbWUgP1xuICAgICAgICAgICAgICAgICAgICAgICAgcmV0dXJuIGh5ZHJhdGVQcm9wcyhcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgY29ubmVjdCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBkaXNjb25uZWN0LFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uQ29udGV4dFxuICAgICAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICByZXR1cm4gYztcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgY29uc3QgbmV3UHJvcHM6IHtba2V5OiBzdHJpbmddOiBhbnl9ID0gaHlkcmF0ZVByb3BzKFxuICAgICAgICAgICAgICAgICAgICBjLmFzcGVjdHMsXG4gICAgICAgICAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgICAgICAgICAgICAgICAgIGNvbm5lY3QsXG4gICAgICAgICAgICAgICAgICAgIGRpc2Nvbm5lY3QsXG4gICAgICAgICAgICAgICAgICAgIG9uQ29udGV4dFxuICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgaWYgKCFuZXdQcm9wcy5rZXkpIHtcbiAgICAgICAgICAgICAgICAgICAgbmV3UHJvcHMua2V5ID0gYy5pZGVudGl0eTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgcmV0dXJuIGh5ZHJhdGVDb21wb25lbnQoXG4gICAgICAgICAgICAgICAgICAgIGMubmFtZSxcbiAgICAgICAgICAgICAgICAgICAgYy5wYWNrYWdlLFxuICAgICAgICAgICAgICAgICAgICBjLmlkZW50aXR5LFxuICAgICAgICAgICAgICAgICAgICBuZXdQcm9wcyxcbiAgICAgICAgICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyxcbiAgICAgICAgICAgICAgICAgICAgY29ubmVjdCxcbiAgICAgICAgICAgICAgICAgICAgZGlzY29ubmVjdCxcbiAgICAgICAgICAgICAgICAgICAgb25Db250ZXh0XG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICB9IGVsc2UgaWYgKGlzQ29tcG9uZW50KHYpKSB7XG4gICAgICAgICAgICBjb25zdCBuZXdQcm9wcyA9IGh5ZHJhdGVQcm9wcyhcbiAgICAgICAgICAgICAgICB2LmFzcGVjdHMsXG4gICAgICAgICAgICAgICAgdXBkYXRlQXNwZWN0cyxcbiAgICAgICAgICAgICAgICBjb25uZWN0LFxuICAgICAgICAgICAgICAgIGRpc2Nvbm5lY3QsXG4gICAgICAgICAgICAgICAgb25Db250ZXh0XG4gICAgICAgICAgICApO1xuICAgICAgICAgICAgcmVwbGFjZVtrXSA9IGh5ZHJhdGVDb21wb25lbnQoXG4gICAgICAgICAgICAgICAgdi5uYW1lLFxuICAgICAgICAgICAgICAgIHYucGFja2FnZSxcbiAgICAgICAgICAgICAgICB2LmlkZW50aXR5LFxuICAgICAgICAgICAgICAgIG5ld1Byb3BzLFxuICAgICAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgICAgICAgICAgICAgY29ubmVjdCxcbiAgICAgICAgICAgICAgICBkaXNjb25uZWN0LFxuICAgICAgICAgICAgICAgIG9uQ29udGV4dFxuICAgICAgICAgICAgKTtcbiAgICAgICAgfSBlbHNlIGlmICh0eXBlKHYpID09PSAnT2JqZWN0Jykge1xuICAgICAgICAgICAgcmVwbGFjZVtrXSA9IGh5ZHJhdGVQcm9wcyhcbiAgICAgICAgICAgICAgICB2LFxuICAgICAgICAgICAgICAgIHVwZGF0ZUFzcGVjdHMsXG4gICAgICAgICAgICAgICAgY29ubmVjdCxcbiAgICAgICAgICAgICAgICBkaXNjb25uZWN0LFxuICAgICAgICAgICAgICAgIG9uQ29udGV4dFxuICAgICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiB7Li4ucHJvcHMsIC4uLnJlcGxhY2V9O1xufVxuXG5leHBvcnQgZnVuY3Rpb24gaHlkcmF0ZUNvbXBvbmVudChcbiAgICBuYW1lOiBzdHJpbmcsXG4gICAgcGFja2FnZV9uYW1lOiBzdHJpbmcsXG4gICAgaWRlbnRpdHk6IHN0cmluZyxcbiAgICBwcm9wczogQW55RGljdCxcbiAgICB1cGRhdGVBc3BlY3RzOiBXcmFwcGVyVXBkYXRlQXNwZWN0RnVuYyxcbiAgICBjb25uZWN0OiBDb25uZWN0RnVuYyxcbiAgICBkaXNjb25uZWN0OiBEaXNjb25uZWN0RnVuYyxcbiAgICBvbkNvbnRleHQ6IEZ1bmN0aW9uXG4pIHtcbiAgICBjb25zdCBwYWNrID0gd2luZG93W3BhY2thZ2VfbmFtZV07XG4gICAgaWYgKCFwYWNrKSB7XG4gICAgICAgIHRocm93IG5ldyBFcnJvcihgSW52YWxpZCBwYWNrYWdlIG5hbWU6ICR7cGFja2FnZV9uYW1lfWApO1xuICAgIH1cbiAgICBjb25zdCBjb21wb25lbnQgPSBwYWNrW25hbWVdO1xuICAgIGlmICghY29tcG9uZW50KSB7XG4gICAgICAgIHRocm93IG5ldyBFcnJvcihgSW52YWxpZCBjb21wb25lbnQgbmFtZTogJHtwYWNrYWdlX25hbWV9LiR7bmFtZX1gKTtcbiAgICB9XG4gICAgLy8gQHRzLWlnbm9yZVxuICAgIGNvbnN0IGVsZW1lbnQgPSBSZWFjdC5jcmVhdGVFbGVtZW50KGNvbXBvbmVudCwgcHJvcHMpO1xuXG4gICAgLyogZXNsaW50LWRpc2FibGUgcmVhY3QvcHJvcC10eXBlcyAqL1xuICAgIGNvbnN0IHdyYXBwZXIgPSAoe2NoaWxkcmVufToge2NoaWxkcmVuPzogYW55fSkgPT4gKFxuICAgICAgICA8V3JhcHBlclxuICAgICAgICAgICAgaWRlbnRpdHk9e2lkZW50aXR5fVxuICAgICAgICAgICAgdXBkYXRlQXNwZWN0cz17dXBkYXRlQXNwZWN0c31cbiAgICAgICAgICAgIGNvbXBvbmVudD17ZWxlbWVudH1cbiAgICAgICAgICAgIGNvbm5lY3Q9e2Nvbm5lY3R9XG4gICAgICAgICAgICBwYWNrYWdlX25hbWU9e3BhY2thZ2VfbmFtZX1cbiAgICAgICAgICAgIGNvbXBvbmVudF9uYW1lPXtuYW1lfVxuICAgICAgICAgICAgYXNwZWN0cz17e2NoaWxkcmVuLCAuLi5wcm9wc319XG4gICAgICAgICAgICBkaXNjb25uZWN0PXtkaXNjb25uZWN0fVxuICAgICAgICAgICAga2V5PXtgd3JhcHBlci0ke2lkZW50aXR5fWB9XG4gICAgICAgIC8+XG4gICAgKTtcblxuICAgIGlmIChjb21wb25lbnQuaXNDb250ZXh0KSB7XG4gICAgICAgIG9uQ29udGV4dCh3cmFwcGVyKTtcbiAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxuICAgIHJldHVybiB3cmFwcGVyKHt9KTtcbn1cblxuZXhwb3J0IGZ1bmN0aW9uIHByZXBhcmVQcm9wKHByb3A6IGFueSkge1xuICAgIGlmIChSZWFjdC5pc1ZhbGlkRWxlbWVudChwcm9wKSkge1xuICAgICAgICAvLyBAdHMtaWdub3JlXG4gICAgICAgIGNvbnN0IHByb3BzOiBXcmFwcGVyUHJvcHMgPSBwcm9wLnByb3BzO1xuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgaWRlbnRpdHk6IHByb3BzLmlkZW50aXR5LFxuICAgICAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICAgICAgYXNwZWN0czogbWFwKFxuICAgICAgICAgICAgICAgIHByZXBhcmVQcm9wLFxuICAgICAgICAgICAgICAgIG9taXQoXG4gICAgICAgICAgICAgICAgICAgIFtcbiAgICAgICAgICAgICAgICAgICAgICAgICdpZGVudGl0eScsXG4gICAgICAgICAgICAgICAgICAgICAgICAndXBkYXRlQXNwZWN0cycsXG4gICAgICAgICAgICAgICAgICAgICAgICAnX25hbWUnLFxuICAgICAgICAgICAgICAgICAgICAgICAgJ19wYWNrYWdlJyxcbiAgICAgICAgICAgICAgICAgICAgICAgICdhc3BlY3RzJyxcbiAgICAgICAgICAgICAgICAgICAgICAgICdrZXknLFxuICAgICAgICAgICAgICAgICAgICBdLFxuICAgICAgICAgICAgICAgICAgICBwcm9wcy5hc3BlY3RzXG4gICAgICAgICAgICAgICAgKVxuICAgICAgICAgICAgKSxcbiAgICAgICAgICAgIG5hbWU6IHByb3BzLmNvbXBvbmVudF9uYW1lLFxuICAgICAgICAgICAgcGFja2FnZTogcHJvcHMucGFja2FnZV9uYW1lLFxuICAgICAgICB9O1xuICAgIH1cbiAgICBpZiAodHlwZShwcm9wKSA9PT0gJ0FycmF5Jykge1xuICAgICAgICByZXR1cm4gcHJvcC5tYXAocHJlcGFyZVByb3ApO1xuICAgIH1cbiAgICBpZiAodHlwZShwcm9wKSA9PT0gJ09iamVjdCcpIHtcbiAgICAgICAgcmV0dXJuIG1hcChwcmVwYXJlUHJvcCwgcHJvcCk7XG4gICAgfVxuICAgIHJldHVybiBwcm9wO1xufVxuIiwiaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCBSZWFjdERPTSBmcm9tICdyZWFjdC1kb20nO1xuaW1wb3J0IFJlbmRlcmVyIGZyb20gJy4vY29tcG9uZW50cy9SZW5kZXJlcic7XG5pbXBvcnQge1JlbmRlck9wdGlvbnN9IGZyb20gJy4vdHlwZXMnO1xuXG5mdW5jdGlvbiByZW5kZXIoXG4gICAge2Jhc2VVcmwsIHBpbmcsIHBpbmdfaW50ZXJ2YWwsIHJldHJpZXN9OiBSZW5kZXJPcHRpb25zLFxuICAgIGVsZW1lbnQ6IHN0cmluZ1xuKSB7XG4gICAgUmVhY3RET00ucmVuZGVyKFxuICAgICAgICA8UmVuZGVyZXJcbiAgICAgICAgICAgIGJhc2VVcmw9e2Jhc2VVcmx9XG4gICAgICAgICAgICBwaW5nPXtwaW5nfVxuICAgICAgICAgICAgcGluZ19pbnRlcnZhbD17cGluZ19pbnRlcnZhbH1cbiAgICAgICAgICAgIHJldHJpZXM9e3JldHJpZXN9XG4gICAgICAgIC8+LFxuICAgICAgICBlbGVtZW50XG4gICAgKTtcbn1cblxuLy8gQHRzLWlnbm9yZVxuZXhwb3J0IHtSZW5kZXJlciwgcmVuZGVyfTtcbiIsIi8qIGVzbGludC1kaXNhYmxlIG5vLW1hZ2ljLW51bWJlcnMgKi9cblxuaW1wb3J0IHtYaHJSZXF1ZXN0T3B0aW9uc30gZnJvbSAnLi90eXBlcyc7XG5cbmNvbnN0IGpzb25QYXR0ZXJuID0gL2pzb24vaTtcblxuY29uc3QgZGVmYXVsdFhock9wdGlvbnM6IFhoclJlcXVlc3RPcHRpb25zID0ge1xuICAgIG1ldGhvZDogJ0dFVCcsXG4gICAgaGVhZGVyczoge30sXG4gICAgcGF5bG9hZDogJycsXG4gICAganNvbjogdHJ1ZSxcbn07XG5cbmV4cG9ydCBjb25zdCBKU09OSEVBREVSUyA9IHtcbiAgICAnQ29udGVudC1UeXBlJzogJ2FwcGxpY2F0aW9uL2pzb24nLFxufTtcblxuZXhwb3J0IGZ1bmN0aW9uIHhoclJlcXVlc3QodXJsOiBzdHJpbmcsIG9wdGlvbnM6IFhoclJlcXVlc3RPcHRpb25zID0gZGVmYXVsdFhock9wdGlvbnMpIHtcbiAgICByZXR1cm4gbmV3IFByb21pc2U8YW55PigocmVzb2x2ZSwgcmVqZWN0KSA9PiB7XG4gICAgICAgIGNvbnN0IHttZXRob2QsIGhlYWRlcnMsIHBheWxvYWQsIGpzb259ID0ge1xuICAgICAgICAgICAgLi4uZGVmYXVsdFhock9wdGlvbnMsXG4gICAgICAgICAgICAuLi5vcHRpb25zLFxuICAgICAgICB9O1xuICAgICAgICBjb25zdCB4aHIgPSBuZXcgWE1MSHR0cFJlcXVlc3QoKTtcbiAgICAgICAgeGhyLm9wZW4obWV0aG9kLCB1cmwpO1xuICAgICAgICBjb25zdCBoZWFkID0ganNvbiA/IHsuLi5KU09OSEVBREVSUywgLi4uaGVhZGVyc30gOiBoZWFkZXJzO1xuICAgICAgICBPYmplY3Qua2V5cyhoZWFkKS5mb3JFYWNoKGsgPT4geGhyLnNldFJlcXVlc3RIZWFkZXIoaywgaGVhZFtrXSkpO1xuICAgICAgICB4aHIub25yZWFkeXN0YXRlY2hhbmdlID0gKCkgPT4ge1xuICAgICAgICAgICAgaWYgKHhoci5yZWFkeVN0YXRlID09PSBYTUxIdHRwUmVxdWVzdC5ET05FKSB7XG4gICAgICAgICAgICAgICAgaWYgKHhoci5zdGF0dXMgPT09IDIwMCkge1xuICAgICAgICAgICAgICAgICAgICBsZXQgcmVzcG9uc2VWYWx1ZSA9IHhoci5yZXNwb25zZTtcbiAgICAgICAgICAgICAgICAgICAgaWYgKFxuICAgICAgICAgICAgICAgICAgICAgICAganNvblBhdHRlcm4udGVzdCh4aHIuZ2V0UmVzcG9uc2VIZWFkZXIoJ0NvbnRlbnQtVHlwZScpKVxuICAgICAgICAgICAgICAgICAgICApIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIHJlc3BvbnNlVmFsdWUgPSBKU09OLnBhcnNlKHhoci5yZXNwb25zZVRleHQpO1xuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIHJlc29sdmUocmVzcG9uc2VWYWx1ZSk7XG4gICAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICAgICAgcmVqZWN0KHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGVycm9yOiAnUmVxdWVzdEVycm9yJyxcbiAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IGBYSFIgJHt1cmx9IEZBSUxFRCAtIFNUQVRVUzogJHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB4aHIuc3RhdHVzXG4gICAgICAgICAgICAgICAgICAgICAgICB9IE1FU1NBR0U6ICR7eGhyLnN0YXR1c1RleHR9YCxcbiAgICAgICAgICAgICAgICAgICAgICAgIHN0YXR1czogeGhyLnN0YXR1cyxcbiAgICAgICAgICAgICAgICAgICAgICAgIHhocixcbiAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9O1xuICAgICAgICB4aHIub25lcnJvciA9IGVyciA9PiByZWplY3QoZXJyKTtcbiAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICB4aHIuc2VuZChqc29uID8gSlNPTi5zdHJpbmdpZnkocGF5bG9hZCkgOiBwYXlsb2FkKTtcbiAgICB9KTtcbn1cblxuZXhwb3J0IGZ1bmN0aW9uIGFwaVJlcXVlc3QoYmFzZVVybDogc3RyaW5nKSB7XG4gICAgcmV0dXJuIGZ1bmN0aW9uKCkge1xuICAgICAgICBjb25zdCB1cmwgPSBiYXNlVXJsICsgYXJndW1lbnRzWzBdO1xuICAgICAgICBjb25zdCBvcHRpb25zID0gYXJndW1lbnRzWzFdIHx8IHt9O1xuICAgICAgICBvcHRpb25zLmhlYWRlcnMgPSB7Li4ub3B0aW9ucy5oZWFkZXJzfTtcbiAgICAgICAgcmV0dXJuIG5ldyBQcm9taXNlKHJlc29sdmUgPT4ge1xuICAgICAgICAgICAgeGhyUmVxdWVzdCh1cmwsIG9wdGlvbnMpLnRoZW4ocmVzb2x2ZSk7XG4gICAgICAgIH0pO1xuICAgIH07XG59XG4iLCJpbXBvcnQge2xvYWRDc3MsIGxvYWRTY3JpcHR9IGZyb20gJ2NvbW1vbnMnO1xuaW1wb3J0IHtQYWNrYWdlLCBSZXF1aXJlbWVudH0gZnJvbSAnLi90eXBlcyc7XG5pbXBvcnQge2Ryb3B9IGZyb20gJ3JhbWRhJztcblxuZXhwb3J0IGZ1bmN0aW9uIGxvYWRSZXF1aXJlbWVudChyZXF1aXJlbWVudDogUmVxdWlyZW1lbnQpIHtcbiAgICByZXR1cm4gbmV3IFByb21pc2U8dm9pZD4oKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICAgICAgICBjb25zdCB7dXJsLCBraW5kfSA9IHJlcXVpcmVtZW50O1xuICAgICAgICBsZXQgbWV0aG9kO1xuICAgICAgICBpZiAoa2luZCA9PT0gJ2pzJykge1xuICAgICAgICAgICAgbWV0aG9kID0gbG9hZFNjcmlwdDtcbiAgICAgICAgfSBlbHNlIGlmIChraW5kID09PSAnY3NzJykge1xuICAgICAgICAgICAgbWV0aG9kID0gbG9hZENzcztcbiAgICAgICAgfSBlbHNlIGlmIChraW5kID09PSAnbWFwJykge1xuICAgICAgICAgICAgcmV0dXJuIHJlc29sdmUoKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHJldHVybiByZWplY3Qoe2Vycm9yOiBgSW52YWxpZCByZXF1aXJlbWVudCBraW5kOiAke2tpbmR9YH0pO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBtZXRob2QodXJsKS50aGVuKHJlc29sdmUpLmNhdGNoKHJlamVjdCk7XG4gICAgfSk7XG59XG5cbmZ1bmN0aW9uIGxvYWRPbmVCeU9uZShyZXF1aXJlbWVudHM6IFJlcXVpcmVtZW50W10pIHtcbiAgICByZXR1cm4gbmV3IFByb21pc2UoKHJlc29sdmUpID0+IHtcbiAgICAgICAgY29uc3QgaGFuZGxlID0gKHJlcXMpID0+IHtcbiAgICAgICAgICAgIGlmIChyZXFzLmxlbmd0aCkge1xuICAgICAgICAgICAgICAgIGNvbnN0IHJlcXVpcmVtZW50ID0gcmVxc1swXTtcbiAgICAgICAgICAgICAgICBsb2FkUmVxdWlyZW1lbnQocmVxdWlyZW1lbnQpLnRoZW4oKCkgPT4gaGFuZGxlKGRyb3AoMSwgcmVxcykpKTtcbiAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgcmVzb2x2ZShudWxsKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfTtcbiAgICAgICAgaGFuZGxlKHJlcXVpcmVtZW50cyk7XG4gICAgfSk7XG59XG5cbmV4cG9ydCBmdW5jdGlvbiBsb2FkUmVxdWlyZW1lbnRzKFxuICAgIHJlcXVpcmVtZW50czogUmVxdWlyZW1lbnRbXSxcbiAgICBwYWNrYWdlczoge1trOiBzdHJpbmddOiBQYWNrYWdlfVxuKSB7XG4gICAgcmV0dXJuIG5ldyBQcm9taXNlPHZvaWQ+KChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgICAgICAgbGV0IGxvYWRpbmdzID0gW107XG4gICAgICAgIE9iamVjdC5rZXlzKHBhY2thZ2VzKS5mb3JFYWNoKChwYWNrX25hbWUpID0+IHtcbiAgICAgICAgICAgIGNvbnN0IHBhY2sgPSBwYWNrYWdlc1twYWNrX25hbWVdO1xuICAgICAgICAgICAgbG9hZGluZ3MgPSBsb2FkaW5ncy5jb25jYXQoXG4gICAgICAgICAgICAgICAgbG9hZE9uZUJ5T25lKHBhY2sucmVxdWlyZW1lbnRzLmZpbHRlcigocikgPT4gci5raW5kID09PSAnanMnKSlcbiAgICAgICAgICAgICk7XG4gICAgICAgICAgICBsb2FkaW5ncyA9IGxvYWRpbmdzLmNvbmNhdChcbiAgICAgICAgICAgICAgICBwYWNrLnJlcXVpcmVtZW50c1xuICAgICAgICAgICAgICAgICAgICAuZmlsdGVyKChyKSA9PiByLmtpbmQgPT09ICdjc3MnKVxuICAgICAgICAgICAgICAgICAgICAubWFwKGxvYWRSZXF1aXJlbWVudClcbiAgICAgICAgICAgICk7XG4gICAgICAgIH0pO1xuICAgICAgICAvLyBUaGVuIGxvYWQgcmVxdWlyZW1lbnRzIHNvIHRoZXkgY2FuIHVzZSBwYWNrYWdlc1xuICAgICAgICAvLyBhbmQgb3ZlcnJpZGUgY3NzLlxuICAgICAgICBQcm9taXNlLmFsbChsb2FkaW5ncylcbiAgICAgICAgICAgIC50aGVuKCgpID0+IHtcbiAgICAgICAgICAgICAgICBsZXQgaSA9IDA7XG4gICAgICAgICAgICAgICAgLy8gTG9hZCBpbiBvcmRlci5cbiAgICAgICAgICAgICAgICBjb25zdCBoYW5kbGVyID0gKCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICBpZiAoaSA8IHJlcXVpcmVtZW50cy5sZW5ndGgpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGxvYWRSZXF1aXJlbWVudChyZXF1aXJlbWVudHNbaV0pLnRoZW4oKCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGkrKztcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBoYW5kbGVyKCk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIHJlc29sdmUoKTtcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH07XG4gICAgICAgICAgICAgICAgaGFuZGxlcigpO1xuICAgICAgICAgICAgfSlcbiAgICAgICAgICAgIC5jYXRjaChyZWplY3QpO1xuICAgIH0pO1xufVxuIiwiLyogZXNsaW50LWRpc2FibGUgbm8tdXNlLWJlZm9yZS1kZWZpbmUgKi9cbmltcG9ydCB7XG4gICAgaXMsXG4gICAgc3BsaXQsXG4gICAgaGFzLFxuICAgIHNsaWNlLFxuICAgIGNvbmNhdCxcbiAgICBwaWNrLFxuICAgIHBsdWNrLFxuICAgIG1lcmdlTGVmdCxcbiAgICBtZXJnZVJpZ2h0LFxuICAgIG1lcmdlRGVlcExlZnQsXG4gICAgbWVyZ2VEZWVwUmlnaHQsXG4gICAgZHJvcCxcbiAgICByZXBsYWNlLFxuICAgIHJlZHVjZSxcbiAgICB0b1BhaXJzLFxuICAgIHRyaW0sXG4gICAgdGFrZSxcbiAgICBpbmNsdWRlcyxcbiAgICBmaW5kLFxuICAgIGpvaW4sXG4gICAgcmV2ZXJzZSxcbiAgICB1bmlxLFxuICAgIHppcCxcbiAgICBzb3J0LFxuICAgIGZyb21QYWlycyxcbiAgICBlcXVhbHMsXG59IGZyb20gJ3JhbWRhJztcbmltcG9ydCB7VHJhbnNmb3JtRnVuYywgVHJhbnNmb3JtR2V0QXNwZWN0RnVuY30gZnJvbSAnLi90eXBlcyc7XG5cbmNvbnN0IGlzQXNwZWN0ID0gKG9iajogYW55KTogYm9vbGVhbiA9PlxuICAgIGlzKE9iamVjdCwgb2JqKSAmJiBoYXMoJ2lkZW50aXR5Jywgb2JqKSAmJiBoYXMoJ2FzcGVjdCcsIG9iaik7XG5cbmNvbnN0IGNvZXJjZUFzcGVjdCA9IChvYmo6IGFueSwgZ2V0QXNwZWN0OiBUcmFuc2Zvcm1HZXRBc3BlY3RGdW5jKTogYW55ID0+XG4gICAgaXNBc3BlY3Qob2JqKSA/IGdldEFzcGVjdChvYmouaWRlbnRpdHksIG9iai5hc3BlY3QpIDogb2JqO1xuXG5jb25zdCB0cmFuc2Zvcm1zOiB7W2tleTogc3RyaW5nXTogVHJhbnNmb3JtRnVuY30gPSB7XG4gICAgLyogU3RyaW5nIHRyYW5zZm9ybXMgKi9cbiAgICBUb1VwcGVyOiB2YWx1ZSA9PiB7XG4gICAgICAgIHJldHVybiB2YWx1ZS50b1VwcGVyQ2FzZSgpO1xuICAgIH0sXG4gICAgVG9Mb3dlcjogdmFsdWUgPT4ge1xuICAgICAgICByZXR1cm4gdmFsdWUudG9Mb3dlckNhc2UoKTtcbiAgICB9LFxuICAgIEZvcm1hdDogKHZhbHVlLCBhcmdzKSA9PiB7XG4gICAgICAgIGNvbnN0IHt0ZW1wbGF0ZX0gPSBhcmdzO1xuICAgICAgICBpZiAoaXMoU3RyaW5nLCB2YWx1ZSkgfHwgaXMoTnVtYmVyLCB2YWx1ZSkgfHwgaXMoQm9vbGVhbiwgdmFsdWUpKSB7XG4gICAgICAgICAgICByZXR1cm4gcmVwbGFjZSgnJHt2YWx1ZX0nLCB2YWx1ZSwgdGVtcGxhdGUpO1xuICAgICAgICB9IGVsc2UgaWYgKGlzKE9iamVjdCwgdmFsdWUpKSB7XG4gICAgICAgICAgICByZXR1cm4gcmVkdWNlKFxuICAgICAgICAgICAgICAgIChhY2MsIFtrLCB2XSkgPT4gcmVwbGFjZShgJFxceyR7a319YCwgdiwgYWNjKSxcbiAgICAgICAgICAgICAgICB0ZW1wbGF0ZSxcbiAgICAgICAgICAgICAgICB0b1BhaXJzKHZhbHVlKVxuICAgICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gdmFsdWU7XG4gICAgfSxcbiAgICBTcGxpdDogKHZhbHVlLCBhcmdzKSA9PiB7XG4gICAgICAgIGNvbnN0IHtzZXBhcmF0b3J9ID0gYXJncztcbiAgICAgICAgcmV0dXJuIHNwbGl0KHNlcGFyYXRvciwgdmFsdWUpO1xuICAgIH0sXG4gICAgVHJpbTogdmFsdWUgPT4ge1xuICAgICAgICByZXR1cm4gdHJpbSh2YWx1ZSk7XG4gICAgfSxcbiAgICAvKiBOdW1iZXIgVHJhbnNmb3JtICovXG4gICAgQWRkOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICBpZiAoaXMoTnVtYmVyLCBhcmdzLnZhbHVlKSkge1xuICAgICAgICAgICAgcmV0dXJuIHZhbHVlICsgYXJncy52YWx1ZTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gdmFsdWUgKyBjb2VyY2VBc3BlY3QoYXJncy52YWx1ZSwgZ2V0QXNwZWN0KTtcbiAgICB9LFxuICAgIFN1YjogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgaWYgKGlzKE51bWJlciwgYXJncy52YWx1ZSkpIHtcbiAgICAgICAgICAgIHJldHVybiB2YWx1ZSAtIGFyZ3MudmFsdWU7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHZhbHVlIC0gY29lcmNlQXNwZWN0KGFyZ3MudmFsdWUsIGdldEFzcGVjdCk7XG4gICAgfSxcbiAgICBEaXZpZGU6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGlmIChpcyhOdW1iZXIsIGFyZ3MudmFsdWUpKSB7XG4gICAgICAgICAgICByZXR1cm4gdmFsdWUgLyBhcmdzLnZhbHVlO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB2YWx1ZSAvIGNvZXJjZUFzcGVjdChhcmdzLnZhbHVlLCBnZXRBc3BlY3QpO1xuICAgIH0sXG4gICAgTXVsdGlwbHk6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGlmIChpcyhOdW1iZXIsIGFyZ3MudmFsdWUpKSB7XG4gICAgICAgICAgICByZXR1cm4gdmFsdWUgKiBhcmdzLnZhbHVlO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB2YWx1ZSAqIGNvZXJjZUFzcGVjdChhcmdzLnZhbHVlLCBnZXRBc3BlY3QpO1xuICAgIH0sXG4gICAgTW9kdWx1czogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgaWYgKGlzKE51bWJlciwgYXJncy52YWx1ZSkpIHtcbiAgICAgICAgICAgIHJldHVybiB2YWx1ZSAlIGFyZ3MudmFsdWU7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHZhbHVlICUgY29lcmNlQXNwZWN0KGFyZ3MudmFsdWUsIGdldEFzcGVjdCk7XG4gICAgfSxcbiAgICBUb1ByZWNpc2lvbjogKHZhbHVlLCBhcmdzKSA9PiB7XG4gICAgICAgIHJldHVybiB2YWx1ZS50b1ByZWNpc2lvbihhcmdzLnByZWNpc2lvbik7XG4gICAgfSxcbiAgICAvKiBBcnJheSB0cmFuc2Zvcm1zICAqL1xuICAgIENvbmNhdDogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgY29uc3Qge290aGVyfSA9IGFyZ3M7XG4gICAgICAgIHJldHVybiBjb25jYXQodmFsdWUsIGNvZXJjZUFzcGVjdChvdGhlciwgZ2V0QXNwZWN0KSk7XG4gICAgfSxcbiAgICBTbGljZTogKHZhbHVlLCBhcmdzKSA9PiB7XG4gICAgICAgIHJldHVybiBzbGljZShhcmdzLnN0YXJ0LCBhcmdzLnN0b3AsIHZhbHVlKTtcbiAgICB9LFxuICAgIE1hcDogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgY29uc3Qge3RyYW5zZm9ybX0gPSBhcmdzO1xuICAgICAgICByZXR1cm4gdmFsdWUubWFwKGUgPT5cbiAgICAgICAgICAgIGV4ZWN1dGVUcmFuc2Zvcm0oXG4gICAgICAgICAgICAgICAgdHJhbnNmb3JtLnRyYW5zZm9ybSxcbiAgICAgICAgICAgICAgICBlLFxuICAgICAgICAgICAgICAgIHRyYW5zZm9ybS5hcmdzLFxuICAgICAgICAgICAgICAgIHRyYW5zZm9ybS5uZXh0LFxuICAgICAgICAgICAgICAgIGdldEFzcGVjdFxuICAgICAgICAgICAgKVxuICAgICAgICApO1xuICAgIH0sXG4gICAgRmlsdGVyOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICBjb25zdCB7Y29tcGFyaXNvbn0gPSBhcmdzO1xuICAgICAgICByZXR1cm4gdmFsdWUuZmlsdGVyKGUgPT5cbiAgICAgICAgICAgIGV4ZWN1dGVUcmFuc2Zvcm0oXG4gICAgICAgICAgICAgICAgY29tcGFyaXNvbi50cmFuc2Zvcm0sXG4gICAgICAgICAgICAgICAgZSxcbiAgICAgICAgICAgICAgICBjb21wYXJpc29uLmFyZ3MsXG4gICAgICAgICAgICAgICAgY29tcGFyaXNvbi5uZXh0LFxuICAgICAgICAgICAgICAgIGdldEFzcGVjdFxuICAgICAgICAgICAgKVxuICAgICAgICApO1xuICAgIH0sXG4gICAgUmVkdWNlOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICBjb25zdCB7dHJhbnNmb3JtLCBhY2N1bXVsYXRvcn0gPSBhcmdzO1xuICAgICAgICBjb25zdCBhY2MgPSBjb2VyY2VBc3BlY3QoYWNjdW11bGF0b3IsIGdldEFzcGVjdCk7XG4gICAgICAgIHJldHVybiB2YWx1ZS5yZWR1Y2UoXG4gICAgICAgICAgICAocHJldmlvdXMsIG5leHQpID0+XG4gICAgICAgICAgICAgICAgZXhlY3V0ZVRyYW5zZm9ybShcbiAgICAgICAgICAgICAgICAgICAgdHJhbnNmb3JtLnRyYW5zZm9ybSxcbiAgICAgICAgICAgICAgICAgICAgW3ByZXZpb3VzLCBuZXh0XSxcbiAgICAgICAgICAgICAgICAgICAgdHJhbnNmb3JtLmFyZ3MsXG4gICAgICAgICAgICAgICAgICAgIHRyYW5zZm9ybS5uZXh0LFxuICAgICAgICAgICAgICAgICAgICBnZXRBc3BlY3RcbiAgICAgICAgICAgICAgICApLFxuICAgICAgICAgICAgYWNjXG4gICAgICAgICk7XG4gICAgfSxcbiAgICBQbHVjazogKHZhbHVlLCBhcmdzKSA9PiB7XG4gICAgICAgIGNvbnN0IHtmaWVsZH0gPSBhcmdzO1xuICAgICAgICByZXR1cm4gcGx1Y2soZmllbGQsIHZhbHVlKTtcbiAgICB9LFxuICAgIEFwcGVuZDogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgcmV0dXJuIGNvbmNhdCh2YWx1ZSwgW2NvZXJjZUFzcGVjdChhcmdzLnZhbHVlLCBnZXRBc3BlY3QpXSk7XG4gICAgfSxcbiAgICBQcmVwZW5kOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICByZXR1cm4gY29uY2F0KFtjb2VyY2VBc3BlY3QoYXJncy52YWx1ZSwgZ2V0QXNwZWN0KV0sIHZhbHVlKTtcbiAgICB9LFxuICAgIEluc2VydDogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgY29uc3Qge3RhcmdldCwgZnJvbnR9ID0gYXJncztcbiAgICAgICAgY29uc3QgdCA9IGNvZXJjZUFzcGVjdCh0YXJnZXQsIGdldEFzcGVjdCk7XG4gICAgICAgIHJldHVybiBmcm9udCA/IGNvbmNhdChbdmFsdWVdLCB0KSA6IGNvbmNhdCh0LCBbdmFsdWVdKTtcbiAgICB9LFxuICAgIFRha2U6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGNvbnN0IHtufSA9IGFyZ3M7XG4gICAgICAgIHJldHVybiB0YWtlKGNvZXJjZUFzcGVjdChuLCBnZXRBc3BlY3QpLCB2YWx1ZSk7XG4gICAgfSxcbiAgICBMZW5ndGg6IHZhbHVlID0+IHtcbiAgICAgICAgcmV0dXJuIHZhbHVlLmxlbmd0aDtcbiAgICB9LFxuICAgIFJhbmdlOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICBjb25zdCB7c3RhcnQsIGVuZCwgc3RlcH0gPSBhcmdzO1xuICAgICAgICBjb25zdCBzID0gY29lcmNlQXNwZWN0KHN0YXJ0LCBnZXRBc3BlY3QpO1xuICAgICAgICBjb25zdCBlID0gY29lcmNlQXNwZWN0KGVuZCwgZ2V0QXNwZWN0KTtcbiAgICAgICAgbGV0IGkgPSBzO1xuICAgICAgICBjb25zdCBhcnIgPSBbXTtcbiAgICAgICAgd2hpbGUgKGkgPCBlKSB7XG4gICAgICAgICAgICBhcnIucHVzaChpKTtcbiAgICAgICAgICAgIGkgKz0gc3RlcDtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gYXJyO1xuICAgIH0sXG4gICAgSW5jbHVkZXM6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIHJldHVybiBpbmNsdWRlcyhjb2VyY2VBc3BlY3QoYXJncy52YWx1ZSwgZ2V0QXNwZWN0KSwgdmFsdWUpO1xuICAgIH0sXG4gICAgRmluZDogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgY29uc3Qge2NvbXBhcmlzb259ID0gYXJncztcbiAgICAgICAgcmV0dXJuIGZpbmQoYSA9PlxuICAgICAgICAgICAgZXhlY3V0ZVRyYW5zZm9ybShcbiAgICAgICAgICAgICAgICBjb21wYXJpc29uLnRyYW5zZm9ybSxcbiAgICAgICAgICAgICAgICBhLFxuICAgICAgICAgICAgICAgIGNvbXBhcmlzb24uYXJncyxcbiAgICAgICAgICAgICAgICBjb21wYXJpc29uLm5leHQsXG4gICAgICAgICAgICAgICAgZ2V0QXNwZWN0XG4gICAgICAgICAgICApXG4gICAgICAgICkodmFsdWUpO1xuICAgIH0sXG4gICAgSm9pbjogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgcmV0dXJuIGpvaW4oY29lcmNlQXNwZWN0KGFyZ3Muc2VwYXJhdG9yLCBnZXRBc3BlY3QpLCB2YWx1ZSk7XG4gICAgfSxcbiAgICBTb3J0OiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICBjb25zdCB7dHJhbnNmb3JtfSA9IGFyZ3M7XG4gICAgICAgIHJldHVybiBzb3J0KFxuICAgICAgICAgICAgKGEsIGIpID0+XG4gICAgICAgICAgICAgICAgZXhlY3V0ZVRyYW5zZm9ybShcbiAgICAgICAgICAgICAgICAgICAgdHJhbnNmb3JtLnRyYW5zZm9ybSxcbiAgICAgICAgICAgICAgICAgICAgW2EsIGJdLFxuICAgICAgICAgICAgICAgICAgICB0cmFuc2Zvcm0uYXJncyxcbiAgICAgICAgICAgICAgICAgICAgdHJhbnNmb3JtLm5leHQsXG4gICAgICAgICAgICAgICAgICAgIGdldEFzcGVjdFxuICAgICAgICAgICAgICAgICksXG4gICAgICAgICAgICB2YWx1ZVxuICAgICAgICApO1xuICAgIH0sXG4gICAgUmV2ZXJzZTogdmFsdWUgPT4ge1xuICAgICAgICByZXR1cm4gcmV2ZXJzZSh2YWx1ZSk7XG4gICAgfSxcbiAgICBVbmlxdWU6IHZhbHVlID0+IHtcbiAgICAgICAgcmV0dXJuIHVuaXEodmFsdWUpO1xuICAgIH0sXG4gICAgWmlwOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICByZXR1cm4gemlwKHZhbHVlLCBjb2VyY2VBc3BlY3QoYXJncy52YWx1ZSwgZ2V0QXNwZWN0KSk7XG4gICAgfSxcbiAgICAvKiBPYmplY3QgdHJhbnNmb3JtcyAqL1xuICAgIFBpY2s6ICh2YWx1ZSwgYXJncykgPT4ge1xuICAgICAgICByZXR1cm4gcGljayhhcmdzLmZpZWxkcywgdmFsdWUpO1xuICAgIH0sXG4gICAgR2V0OiAodmFsdWUsIGFyZ3MpID0+IHtcbiAgICAgICAgcmV0dXJuIHZhbHVlW2FyZ3MuZmllbGRdO1xuICAgIH0sXG4gICAgU2V0OiAodiwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGNvbnN0IHtrZXksIHZhbHVlfSA9IGFyZ3M7XG4gICAgICAgIHZba2V5XSA9IGNvZXJjZUFzcGVjdCh2YWx1ZSwgZ2V0QXNwZWN0KTtcbiAgICAgICAgcmV0dXJuIHY7XG4gICAgfSxcbiAgICBQdXQ6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGNvbnN0IHtrZXksIHRhcmdldH0gPSBhcmdzO1xuICAgICAgICBjb25zdCBvYmogPSBjb2VyY2VBc3BlY3QodGFyZ2V0LCBnZXRBc3BlY3QpO1xuICAgICAgICBvYmpba2V5XSA9IHZhbHVlO1xuICAgICAgICByZXR1cm4gb2JqO1xuICAgIH0sXG4gICAgTWVyZ2U6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGNvbnN0IHtkZWVwLCBkaXJlY3Rpb24sIG90aGVyfSA9IGFyZ3M7XG4gICAgICAgIGxldCBvdGhlclZhbHVlID0gb3RoZXI7XG4gICAgICAgIGlmIChpc0FzcGVjdChvdGhlcikpIHtcbiAgICAgICAgICAgIG90aGVyVmFsdWUgPSBnZXRBc3BlY3Qob3RoZXIuaWRlbnRpdHksIG90aGVyLmFzcGVjdCk7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKGRpcmVjdGlvbiA9PT0gJ3JpZ2h0Jykge1xuICAgICAgICAgICAgaWYgKGRlZXApIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gbWVyZ2VEZWVwUmlnaHQodmFsdWUsIG90aGVyVmFsdWUpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgcmV0dXJuIG1lcmdlUmlnaHQodmFsdWUsIG90aGVyVmFsdWUpO1xuICAgICAgICB9XG4gICAgICAgIGlmIChkZWVwKSB7XG4gICAgICAgICAgICByZXR1cm4gbWVyZ2VEZWVwTGVmdCh2YWx1ZSwgb3RoZXJWYWx1ZSk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIG1lcmdlTGVmdCh2YWx1ZSwgb3RoZXJWYWx1ZSk7XG4gICAgfSxcbiAgICBUb0pzb246IHZhbHVlID0+IHtcbiAgICAgICAgcmV0dXJuIEpTT04uc3RyaW5naWZ5KHZhbHVlKTtcbiAgICB9LFxuICAgIEZyb21Kc29uOiB2YWx1ZSA9PiB7XG4gICAgICAgIHJldHVybiBKU09OLnBhcnNlKHZhbHVlKTtcbiAgICB9LFxuICAgIFRvUGFpcnM6IHZhbHVlID0+IHtcbiAgICAgICAgcmV0dXJuIHRvUGFpcnModmFsdWUpO1xuICAgIH0sXG4gICAgRnJvbVBhaXJzOiB2YWx1ZSA9PiB7XG4gICAgICAgIHJldHVybiBmcm9tUGFpcnModmFsdWUpO1xuICAgIH0sXG4gICAgLyogQ29uZGl0aW9uYWxzICovXG4gICAgSWY6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGNvbnN0IHtjb21wYXJpc29uLCB0aGVuLCBvdGhlcndpc2V9ID0gYXJncztcbiAgICAgICAgY29uc3QgYyA9IHRyYW5zZm9ybXNbY29tcGFyaXNvbi50cmFuc2Zvcm1dO1xuXG4gICAgICAgIGlmIChjKHZhbHVlLCBjb21wYXJpc29uLmFyZ3MsIGdldEFzcGVjdCkpIHtcbiAgICAgICAgICAgIHJldHVybiBleGVjdXRlVHJhbnNmb3JtKFxuICAgICAgICAgICAgICAgIHRoZW4udHJhbnNmb3JtLFxuICAgICAgICAgICAgICAgIHZhbHVlLFxuICAgICAgICAgICAgICAgIHRoZW4uYXJncyxcbiAgICAgICAgICAgICAgICB0aGVuLm5leHQsXG4gICAgICAgICAgICAgICAgZ2V0QXNwZWN0XG4gICAgICAgICAgICApO1xuICAgICAgICB9XG4gICAgICAgIGlmIChvdGhlcndpc2UpIHtcbiAgICAgICAgICAgIHJldHVybiBleGVjdXRlVHJhbnNmb3JtKFxuICAgICAgICAgICAgICAgIG90aGVyd2lzZS50cmFuc2Zvcm0sXG4gICAgICAgICAgICAgICAgdmFsdWUsXG4gICAgICAgICAgICAgICAgb3RoZXJ3aXNlLmFyZ3MsXG4gICAgICAgICAgICAgICAgb3RoZXJ3aXNlLm5leHQsXG4gICAgICAgICAgICAgICAgZ2V0QXNwZWN0XG4gICAgICAgICAgICApO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB2YWx1ZTtcbiAgICB9LFxuICAgIEVxdWFsczogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgcmV0dXJuIGVxdWFscyh2YWx1ZSwgY29lcmNlQXNwZWN0KGFyZ3Mub3RoZXIsIGdldEFzcGVjdCkpO1xuICAgIH0sXG4gICAgTm90RXF1YWxzOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICByZXR1cm4gIWVxdWFscyh2YWx1ZSwgY29lcmNlQXNwZWN0KGFyZ3Mub3RoZXIsIGdldEFzcGVjdCkpO1xuICAgIH0sXG4gICAgTWF0Y2g6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIGNvbnN0IHIgPSBuZXcgUmVnRXhwKGNvZXJjZUFzcGVjdChhcmdzLm90aGVyLCBnZXRBc3BlY3QpKTtcbiAgICAgICAgcmV0dXJuIHIudGVzdCh2YWx1ZSk7XG4gICAgfSxcbiAgICBHcmVhdGVyOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICByZXR1cm4gdmFsdWUgPiBjb2VyY2VBc3BlY3QoYXJncy5vdGhlciwgZ2V0QXNwZWN0KTtcbiAgICB9LFxuICAgIEdyZWF0ZXJPckVxdWFsczogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgcmV0dXJuIHZhbHVlID49IGNvZXJjZUFzcGVjdChhcmdzLm90aGVyLCBnZXRBc3BlY3QpO1xuICAgIH0sXG4gICAgTGVzc2VyOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICByZXR1cm4gdmFsdWUgPCBjb2VyY2VBc3BlY3QoYXJncy5vdGhlciwgZ2V0QXNwZWN0KTtcbiAgICB9LFxuICAgIExlc3Nlck9yRXF1YWxzOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICByZXR1cm4gdmFsdWUgPD0gY29lcmNlQXNwZWN0KGFyZ3Mub3RoZXIsIGdldEFzcGVjdCk7XG4gICAgfSxcbiAgICBBbmQ6ICh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KSA9PiB7XG4gICAgICAgIHJldHVybiB2YWx1ZSAmJiBjb2VyY2VBc3BlY3QoYXJncy5vdGhlciwgZ2V0QXNwZWN0KTtcbiAgICB9LFxuICAgIE9yOiAodmFsdWUsIGFyZ3MsIGdldEFzcGVjdCkgPT4ge1xuICAgICAgICByZXR1cm4gdmFsdWUgfHwgY29lcmNlQXNwZWN0KGFyZ3Mub3RoZXIsIGdldEFzcGVjdCk7XG4gICAgfSxcbiAgICBOb3Q6IHZhbHVlID0+IHtcbiAgICAgICAgcmV0dXJuICF2YWx1ZTtcbiAgICB9LFxuICAgIFJhd1ZhbHVlOiAodmFsdWUsIGFyZ3MpID0+IHtcbiAgICAgICAgcmV0dXJuIGFyZ3MudmFsdWU7XG4gICAgfSxcbiAgICBBc3BlY3RWYWx1ZTogKHZhbHVlLCBhcmdzLCBnZXRBc3BlY3QpID0+IHtcbiAgICAgICAgY29uc3Qge2lkZW50aXR5LCBhc3BlY3R9ID0gYXJncy50YXJnZXQ7XG4gICAgICAgIHJldHVybiBnZXRBc3BlY3QoaWRlbnRpdHksIGFzcGVjdCk7XG4gICAgfSxcbn07XG5cbmV4cG9ydCBjb25zdCBleGVjdXRlVHJhbnNmb3JtID0gKFxuICAgIHRyYW5zZm9ybTogc3RyaW5nLFxuICAgIHZhbHVlOiBhbnksXG4gICAgYXJnczogYW55LFxuICAgIG5leHQ6IEFycmF5PGFueT4sXG4gICAgZ2V0QXNwZWN0OiBUcmFuc2Zvcm1HZXRBc3BlY3RGdW5jXG4pID0+IHtcbiAgICBjb25zdCB0ID0gdHJhbnNmb3Jtc1t0cmFuc2Zvcm1dO1xuICAgIGNvbnN0IG5ld1ZhbHVlID0gdCh2YWx1ZSwgYXJncywgZ2V0QXNwZWN0KTtcbiAgICBpZiAobmV4dC5sZW5ndGgpIHtcbiAgICAgICAgY29uc3QgbiA9IG5leHRbMF07XG4gICAgICAgIHJldHVybiBleGVjdXRlVHJhbnNmb3JtKFxuICAgICAgICAgICAgbi50cmFuc2Zvcm0sXG4gICAgICAgICAgICBuZXdWYWx1ZSxcbiAgICAgICAgICAgIG4uYXJncyxcbiAgICAgICAgICAgIC8vIEV4ZWN1dGUgdGhlIG5leHQgZmlyc3QsIHRoZW4gYmFjayB0byBjaGFpbi5cbiAgICAgICAgICAgIGNvbmNhdChuLm5leHQsIGRyb3AoMSwgbmV4dCkpLFxuICAgICAgICAgICAgZ2V0QXNwZWN0XG4gICAgICAgICk7XG4gICAgfVxuICAgIHJldHVybiBuZXdWYWx1ZTtcbn07XG5cbmV4cG9ydCBkZWZhdWx0IHRyYW5zZm9ybXM7XG4iLCJtb2R1bGUuZXhwb3J0cyA9IF9fV0VCUEFDS19FWFRFUk5BTF9NT0RVTEVfcmVhY3RfXzsiLCJtb2R1bGUuZXhwb3J0cyA9IF9fV0VCUEFDS19FWFRFUk5BTF9NT0RVTEVfcmVhY3RfZG9tX187Il0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9