(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2feb823c"],{1331:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=(0,i.regex)("integer",/(^[0-9]*$)|(^-[0-9]+$)/);t.default=a},"29b0":function(e,t,r){"use strict";var i=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("div",{staticClass:"account-pages my-5 pt-5"},[r("div",{staticClass:"container"},[e._t("default")],2)])])},a=[],n={components:{}},s=n,u=r("2877"),o=Object(u["a"])(s,i,a,!1,null,null,null);t["a"]=o.exports},"2a12":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"maxLength",max:e},(function(t){return!(0,i.req)(t)||(0,i.len)(t)<=e}))};t.default=a},3360:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(){for(var e=arguments.length,t=new Array(e),r=0;r<e;r++)t[r]=arguments[r];return(0,i.withParams)({type:"and"},(function(){for(var e=this,r=arguments.length,i=new Array(r),a=0;a<r;a++)i[a]=arguments[a];return t.length>0&&t.reduce((function(t,r){return t&&r.apply(e,i)}),!0)}))};t.default=a},"3a54":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=(0,i.regex)("alphaNum",/^[a-zA-Z0-9]*$/);t.default=a},"45b8":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=(0,i.regex)("numeric",/^[0-9]*$/);t.default=a},"46bc":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"maxValue",max:e},(function(t){return!(0,i.req)(t)||(!/\s/.test(t)||t instanceof Date)&&+t<=+e}))};t.default=a},"5d75":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=/^(?:[A-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]{2,}(?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/,n=(0,i.regex)("email",a);t.default=n},"5db3":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"minLength",min:e},(function(t){return!(0,i.req)(t)||(0,i.len)(t)>=e}))};t.default=a},6235:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=(0,i.regex)("alpha",/^[a-zA-Z]*$/);t.default=a},6417:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"not"},(function(t,r){return!(0,i.req)(t)||!e.call(this,t,r)}))};t.default=a},7006:function(e,t,r){e.exports=r.p+"../static/img/profile-img.ba4e037e.png"},"772d":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=/^(?:(?:https?|ftp):\/\/)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:[/?#]\S*)?$/i,n=(0,i.regex)("url",a);t.default=n},"78ef":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"withParams",{enumerable:!0,get:function(){return i.default}}),t.regex=t.ref=t.len=t.req=void 0;var i=a(r("8750"));function a(e){return e&&e.__esModule?e:{default:e}}function n(e){return n="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"===typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},n(e)}var s=function(e){if(Array.isArray(e))return!!e.length;if(void 0===e||null===e)return!1;if(!1===e)return!0;if(e instanceof Date)return!isNaN(e.getTime());if("object"===n(e)){for(var t in e)return!0;return!1}return!!String(e).length};t.req=s;var u=function(e){return Array.isArray(e)?e.length:"object"===n(e)?Object.keys(e).length:String(e).length};t.len=u;var o=function(e,t,r){return"function"===typeof e?e.call(t,r):r[e]};t.ref=o;var l=function(e,t){return(0,i.default)({type:e},(function(e){return!s(e)||t.test(e)}))};t.regex=l},8750:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i="web"===Object({NODE_ENV:"production",VUE_APP_APIKEY:"",VUE_APP_APPId:"",VUE_APP_AUTHDOMAIN:"",VUE_APP_DATABASEURL:"",VUE_APP_DEFAULT_AUTH:"fakebackend",VUE_APP_I18N_FALLBACK_LOCALE:"en",VUE_APP_I18N_LOCALE:"pt",VUE_APP_IMG_URL:"http://192.168.1.191:8000",VUE_APP_KEY:"10246158-7c7ac143286126a2c3e8c9506",VUE_APP_MEASUREMENTID:"",VUE_APP_MESSAGINGSENDERID:"",VUE_APP_PROJECTId:"",VUE_APP_SERVER_URL:"http://192.168.1.191:8000/rest/v1/",VUE_APP_STORAGEBUCKET:"",VUE_APP_URL:"http://localhost:8080/",BASE_URL:"/"}).BUILD?r("cb69").withParams:r("0234").withParams,a=i;t.default=a},"91d3":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:":";return(0,i.withParams)({type:"macAddress"},(function(t){if(!(0,i.req)(t))return!0;if("string"!==typeof t)return!1;var r="string"===typeof e&&""!==e?t.split(e):12===t.length||16===t.length?t.match(/.{2}/g):null;return null!==r&&(6===r.length||8===r.length)&&r.every(n)}))};t.default=a;var n=function(e){return e.toLowerCase().match(/^[0-9a-f]{2}$/)}},aa82:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"requiredIf",prop:e},(function(t,r){return!(0,i.ref)(e,this,r)||(0,i.req)(t)}))};t.default=a},b5ae:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"alpha",{enumerable:!0,get:function(){return i.default}}),Object.defineProperty(t,"alphaNum",{enumerable:!0,get:function(){return a.default}}),Object.defineProperty(t,"numeric",{enumerable:!0,get:function(){return n.default}}),Object.defineProperty(t,"between",{enumerable:!0,get:function(){return s.default}}),Object.defineProperty(t,"email",{enumerable:!0,get:function(){return u.default}}),Object.defineProperty(t,"ipAddress",{enumerable:!0,get:function(){return o.default}}),Object.defineProperty(t,"macAddress",{enumerable:!0,get:function(){return l.default}}),Object.defineProperty(t,"maxLength",{enumerable:!0,get:function(){return c.default}}),Object.defineProperty(t,"minLength",{enumerable:!0,get:function(){return f.default}}),Object.defineProperty(t,"required",{enumerable:!0,get:function(){return d.default}}),Object.defineProperty(t,"requiredIf",{enumerable:!0,get:function(){return m.default}}),Object.defineProperty(t,"requiredUnless",{enumerable:!0,get:function(){return p.default}}),Object.defineProperty(t,"sameAs",{enumerable:!0,get:function(){return b.default}}),Object.defineProperty(t,"url",{enumerable:!0,get:function(){return v.default}}),Object.defineProperty(t,"or",{enumerable:!0,get:function(){return y.default}}),Object.defineProperty(t,"and",{enumerable:!0,get:function(){return g.default}}),Object.defineProperty(t,"not",{enumerable:!0,get:function(){return _.default}}),Object.defineProperty(t,"minValue",{enumerable:!0,get:function(){return P.default}}),Object.defineProperty(t,"maxValue",{enumerable:!0,get:function(){return h.default}}),Object.defineProperty(t,"integer",{enumerable:!0,get:function(){return O.default}}),Object.defineProperty(t,"decimal",{enumerable:!0,get:function(){return j.default}}),t.helpers=void 0;var i=C(r("6235")),a=C(r("3a54")),n=C(r("45b8")),s=C(r("ec11")),u=C(r("5d75")),o=C(r("c99d")),l=C(r("91d3")),c=C(r("2a12")),f=C(r("5db3")),d=C(r("d4f4")),m=C(r("aa82")),p=C(r("e652")),b=C(r("b6cb")),v=C(r("772d")),y=C(r("d294")),g=C(r("3360")),_=C(r("6417")),P=C(r("eb66")),h=C(r("46bc")),O=C(r("1331")),j=C(r("c301")),x=w(r("78ef"));function w(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var r in e)if(Object.prototype.hasOwnProperty.call(e,r)){var i=Object.defineProperty&&Object.getOwnPropertyDescriptor?Object.getOwnPropertyDescriptor(e,r):{};i.get||i.set?Object.defineProperty(t,r,i):t[r]=e[r]}return t.default=e,t}function C(e){return e&&e.__esModule?e:{default:e}}t.helpers=x},b6cb:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"sameAs",eq:e},(function(t,r){return t===(0,i.ref)(e,this,r)}))};t.default=a},c301:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=(0,i.regex)("decimal",/^[-]?\d*(\.\d+)?$/);t.default=a},c99d:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=(0,i.withParams)({type:"ipAddress"},(function(e){if(!(0,i.req)(e))return!0;if("string"!==typeof e)return!1;var t=e.split(".");return 4===t.length&&t.every(n)}));t.default=a;var n=function(e){if(e.length>3||0===e.length)return!1;if("0"===e[0]&&"0"!==e)return!1;if(!e.match(/^\d+$/))return!1;var t=0|+e;return t>=0&&t<=255}},cb69:function(e,t,r){"use strict";(function(e){function r(e){return r="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"===typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},r(e)}Object.defineProperty(t,"__esModule",{value:!0}),t.withParams=void 0;var i="undefined"!==typeof window?window:"undefined"!==typeof e?e:{},a=function(e,t){return"object"===r(e)&&void 0!==t?t:e((function(){}))},n=i.vuelidate?i.vuelidate.withParams:a;t.withParams=n}).call(this,r("c8ba"))},d294:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(){for(var e=arguments.length,t=new Array(e),r=0;r<e;r++)t[r]=arguments[r];return(0,i.withParams)({type:"or"},(function(){for(var e=this,r=arguments.length,i=new Array(r),a=0;a<r;a++)i[a]=arguments[a];return t.length>0&&t.reduce((function(t,r){return t||r.apply(e,i)}),!1)}))};t.default=a},d4f4:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=(0,i.withParams)({type:"required"},(function(e){return"string"===typeof e?(0,i.req)(e.trim()):(0,i.req)(e)}));t.default=a},e347:function(e,t,r){e.exports=r.p+"../static/img/logo.f7686e58.svg"},e652:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"requiredUnless",prop:e},(function(t,r){return!!(0,i.ref)(e,this,r)||(0,i.req)(t)}))};t.default=a},eb66:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e){return(0,i.withParams)({type:"minValue",min:e},(function(t){return!(0,i.req)(t)||(!/\s/.test(t)||t instanceof Date)&&+t>=+e}))};t.default=a},ec11:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i=r("78ef"),a=function(e,t){return(0,i.withParams)({type:"between",min:e,max:t},(function(r){return!(0,i.req)(r)||(!/\s/.test(r)||r instanceof Date)&&+e<=+r&&+t>=+r}))};t.default=a},fc27:function(e,t,r){"use strict";r.r(t);var i=function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("Layout",[i("div",{staticClass:"row justify-content-center"},[i("div",{staticClass:"col-md-8 col-lg-6 col-xl-5"},[i("div",{staticClass:"card overflow-hidden"},[i("div",{staticClass:"bg-soft bg-primary"},[i("div",{staticClass:"row"},[i("div",{staticClass:"col-7"},[i("div",{staticClass:"text-primary p-4"},[i("h5",{staticClass:"text-primary"},[e._v("Free Register")]),i("p",[e._v("Get your free Skote account now.")])])]),i("div",{staticClass:"col-5 align-self-end"},[i("img",{staticClass:"img-fluid",attrs:{src:r("7006"),alt:""}})])])]),i("div",{staticClass:"card-body pt-0"},[i("div",[i("router-link",{attrs:{tag:"a",to:"/"}},[i("div",{staticClass:"avatar-md profile-user-wid mb-4"},[i("span",{staticClass:"avatar-title rounded-circle bg-light"},[i("img",{staticClass:"rounded-circle",attrs:{src:r("e347"),alt:"",height:"34"}})])])])],1),i("b-alert",{staticClass:"mt-3",attrs:{variant:"success",dismissible:""},model:{value:e.registerSuccess,callback:function(t){e.registerSuccess=t},expression:"registerSuccess"}},[e._v("Registration successfull.")]),i("b-alert",{staticClass:"mt-3",attrs:{variant:"danger",dismissible:""},model:{value:e.isRegisterError,callback:function(t){e.isRegisterError=t},expression:"isRegisterError"}},[e._v(e._s(e.regError))]),e.notification.message?i("div",{class:"alert "+e.notification.type},[e._v(" "+e._s(e.notification.message)+" ")]):e._e(),i("b-form",{staticClass:"p-2",on:{submit:function(t){return t.preventDefault(),e.tryToRegisterIn(t)}}},[i("b-form-group",{staticClass:"mb-3",attrs:{id:"email-group",label:"Username","label-for":"username"}},[i("b-form-input",{class:{"is-invalid":e.submitted&&e.$v.user.username.$error},attrs:{id:"username",type:"text",placeholder:"Enter username"},model:{value:e.user.username,callback:function(t){e.$set(e.user,"username",t)},expression:"user.username"}}),e.submitted&&!e.$v.user.username.required?i("div",{staticClass:"invalid-feedback"},[e._v(" Username is required. ")]):e._e()],1),i("b-form-group",{staticClass:"mb-3",attrs:{id:"fullname-group",label:"Email","label-for":"email"}},[i("b-form-input",{class:{"is-invalid":e.submitted&&e.$v.user.email.$error},attrs:{id:"email",type:"email",placeholder:"Enter email"},model:{value:e.user.email,callback:function(t){e.$set(e.user,"email",t)},expression:"user.email"}}),e.submitted&&e.$v.user.email.$error?i("div",{staticClass:"invalid-feedback"},[e.$v.user.email.required?e._e():i("span",[e._v("Email is required.")]),e.$v.user.email.email?e._e():i("span",[e._v("Please enter valid email.")])]):e._e()],1),i("b-form-group",{staticClass:"mb-3",attrs:{id:"password-group",label:"Password","label-for":"password"}},[i("b-form-input",{class:{"is-invalid":e.submitted&&e.$v.user.password.$error},attrs:{id:"password",type:"password",placeholder:"Enter password"},model:{value:e.user.password,callback:function(t){e.$set(e.user,"password",t)},expression:"user.password"}}),e.submitted&&!e.$v.user.password.required?i("div",{staticClass:"invalid-feedback"},[e._v(" Password is required. ")]):e._e()],1),i("div",{staticClass:"mt-4 d-grid"},[i("b-button",{staticClass:"btn-block",attrs:{type:"submit",variant:"primary"}},[e._v("Register")])],1),i("div",{staticClass:"mt-4 text-center"},[i("h5",{staticClass:"font-size-14 mb-3"},[e._v("Sign up using")]),i("ul",{staticClass:"list-inline"},[i("li",{staticClass:"list-inline-item"},[i("a",{staticClass:"social-list-item bg-primary text-white border-primary",attrs:{href:"javascript: void(0);"}},[i("i",{staticClass:"mdi mdi-facebook"})])]),i("li",{staticClass:"list-inline-item"},[i("a",{staticClass:"social-list-item bg-info text-white border-info",attrs:{href:"javascript: void(0);"}},[i("i",{staticClass:"mdi mdi-twitter"})])]),i("li",{staticClass:"list-inline-item"},[i("a",{staticClass:"social-list-item bg-danger text-white border-danger",attrs:{href:"javascript: void(0);"}},[i("i",{staticClass:"mdi mdi-google"})])])])]),i("div",{staticClass:"mt-4 text-center"},[i("p",{staticClass:"mb-0"},[e._v(" By registering you agree to the Skote "),i("a",{staticClass:"text-primary",attrs:{href:"javascript: void(0);"}},[e._v("Terms of Use")])])])],1)],1)]),i("div",{staticClass:"mt-5 text-center"},[i("p",[e._v(" Already have an account ? "),i("router-link",{staticClass:"fw-medium text-primary",attrs:{tag:"a",to:"/login"}},[e._v("Login")])],1),i("p",[e._v(" © "+e._s((new Date).getFullYear())+" Skote. Crafted with "),i("i",{staticClass:"mdi mdi-heart text-danger"}),e._v(" by Themesbrand ")])])])])])},a=[],n=(r("a4d3"),r("e01a"),r("5530")),s=(r("bc3a"),r("4d77")),u=r("29b0"),o=r("c2a4"),l=r("2f62"),c=r("b5ae"),f={page:{title:"Register",meta:[{name:"description",content:o.description}]},components:{Layout:u["a"]},data:function(){return{user:{username:"",email:"",password:""},submitted:!1,regError:null,tryingToRegister:!1,isRegisterError:!1,registerSuccess:!1}},validations:{user:{username:{required:c["required"]},email:{required:c["required"],email:c["email"]},password:{required:c["required"]}}},computed:Object(n["a"])(Object(n["a"])({},Object(l["d"])("authfack",["status"])),{},{notification:function(){return this.$store?this.$store.state.notification:null}}),methods:Object(n["a"])(Object(n["a"])(Object(n["a"])(Object(n["a"])({},s["b"]),s["a"]),s["e"]),{},{tryToRegisterIn:function(){if(this.submitted=!0,this.$v.$touch(),!this.$v.$invalid){var e=this.user,t=e.email,r=e.username,i=e.password;t&&r&&i&&this.registeruser(this.user)}}})},d=f,m=r("2877"),p=Object(m["a"])(d,i,a,!1,null,null,null);t["default"]=p.exports}}]);
//# sourceMappingURL=chunk-2feb823c.f309be74.js.map