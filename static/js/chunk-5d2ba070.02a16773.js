(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5d2ba070"],{"3a1d":function(t,e,r){"use strict";r.r(e);var a=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("div",{staticClass:"container-fluid barraSuperior",attrs:{id:"top"}},[r("div",{staticClass:"container"},[r("b-row",[r("b-col",{staticClass:"social",attrs:{cols:"12",lg:"9",md:"9",sm:"8"}},[r("ul",[r("li",[r("a",{attrs:{href:"http://facebook.com/infinitygroupparaguay",target:"_blank"}},[r("b-icon",{staticClass:"redSocial facebookBlanco",attrs:{icon:"facebook",size:"sm"}})],1)]),r("li",[r("a",{attrs:{href:"http://youtube.com",target:"_blank"}},[r("b-icon",{staticClass:"redSocial youtubeBlanco",attrs:{icon:"youtube",size:"sm"}})],1)]),r("li",[r("a",{attrs:{href:"http://instagram.com/infinitygroupparaguay",target:"_blank"}},[r("b-icon",{staticClass:"redSocial instagramBlanco",attrs:{icon:"instagram",size:"sm"}})],1)]),r("li",[r("a",{attrs:{href:"http://google.com",target:"_blank"}},[r("b-icon",{staticClass:"redSocial googleBlanco",attrs:{icon:"google",size:"sm"}})],1)]),r("li",[r("a",{attrs:{href:"http://twitter.com",target:"_blank"}},[r("b-icon",{staticClass:"redSocial twitterBlanco",attrs:{icon:"twitter",size:"sm"}})],1)])])]),r("b-col",{staticClass:"registro",attrs:{cols:"12",lg:"3",md:"3",sm:"4"}},[r("ul",[r("li",[r("a",{attrs:{href:"#"}},[t._v("Entrar")])]),r("li",[t._v(" | ")]),r("li",[r("a",{attrs:{href:"#"}},[t._v("Criar uma Conta")])])])])],1)],1)]),r("header",{staticClass:"container-fluid"},[r("div",{staticClass:"container"},[r("b-row",{attrs:{id:"cabecalho"}},[r("b-col",{attrs:{cols:"12",lg:"3",md:"3",sm:"2",id:"logotipo"}},[r("a",{attrs:{href:"/home"}},[r("b-img",{attrs:{src:t.imgUrl+"/media/loja/logotipo.png",fluid:"",alt:"Logotipo da loja"}})],1)]),r("b-col",{attrs:{cols:"12",lg:"6",md:"6",sm:"8"}},[r("b-row",[r("b-col",{staticClass:"backColor",attrs:{cols:"12",lg:"4",md:"4",sm:"4",id:"btnCategorias"}},[r("p",[t._v(" CATEGORIAS "),r("span",{staticClass:"pull-right"},[r("b-icon",{attrs:{icon:"border-width","aria-hidden":"true",size:"sm"},on:{click:t.ativarCategorias}})],1)])]),r("b-col",{attrs:{cols:"12",lg:"8",md:"8",sm:"8"}},[r("div",{staticClass:"input-group",attrs:{id:"buscador"}},[r("input",{directives:[{name:"model",rawName:"v-model",value:t.termo,expression:"termo"}],staticClass:"form-control input-custom",attrs:{type:"search",name:"buscar",placeholder:"Buscar"},domProps:{value:t.termo},on:{keypress:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.listarProdutosByName(e)},input:function(e){e.target.composing||(t.termo=e.target.value)}}}),r("span",{staticClass:"input-group-btn"},[r("a",{attrs:{href:"#"}},[r("button",{staticClass:"btn btn-default backColor",on:{click:t.listarProdutosByName}},[r("b-icon",{attrs:{icon:"search",size:"sm"}})],1)]),r("router-link",{attrs:{to:"/home"}},[r("button",{staticClass:"btn btn-default backColor"},[r("b-icon",{attrs:{icon:"search",size:"sm"}})],1)])],1)])])],1)],1),r("b-col",{attrs:{cols:"12",lg:"3",md:"3",sm:"2"}}),r("div",{staticClass:"card"},[t.mostrarCategorias?r("b-col",{staticClass:"backColor",attrs:{cols:"12",id:"categorias"}},[r("b-row",t._l(t.categorias,(function(e){return r("b-col",{key:e.id,attrs:{cols:"12",lg:"2",md:"3",sm:"4"}},[r("ul",[r("h4",{on:{click:function(r){return t.listarProdutosByCategoria(e.id)}}},[r("a",{staticClass:"pixelCategorias",attrs:{href:"#"}},[t._v(t._s(e.descricao))])]),r("hr"),t._l(e.subcategoria,(function(e){return r("li",{key:e.id,staticClass:"backColor",on:{click:function(r){return t.listarProdutosBySubCategoria(e.id)}}},[r("a",{staticClass:"pixelSubCategorias",attrs:{href:"#"}},[t._v(t._s(e.descricao))])])}))],2)])})),1)],1):t._e()],1)],1)],1)]),r("section",{attrs:{id:"banner-loja"}}),t.produtos.length?r("div",{staticClass:"row justify-content-center"},[r("div",{staticClass:"col-lg-9"},[r("div",{staticClass:"row mb-3"},[t._m(0),r("div",{staticClass:"col-lg-8 col-sm-6"},[r("form",{staticClass:"mt-4 mt-sm-0 float-sm-end d-flex align-items-center"},[r("div",{staticClass:"search-box me-2"},[r("div",{staticClass:"position-relative"},[r("input",{staticClass:"form-control border-0",attrs:{type:"text",placeholder:"Buscar..."},on:{input:function(e){return t.searchFilter(e)}}}),r("i",{staticClass:"bx bx-search-alt search-icon"})])]),t._m(1)])])]),r("div",{staticClass:"row"},t._l(t.produtos,(function(e){return r("div",{key:e.id,staticClass:"col-xl-4 col-sm-6"},[r("div",{staticClass:"card p-1 m-1 card-sil",attrs:{id:"card-produto"}},[r("div",{staticClass:"card-body"},[r("div",{staticClass:"product-img position-relative"},[e.discount?r("div",{staticClass:"avatar-sm product-ribbon"},[r("span",{staticClass:"avatar-title rounded-circle bg-primary"},[t._v("-"+t._s(e.discount)+"%")])]):t._e(),r("router-link",{attrs:{to:"/ecommerce/product-detail/"+e.id}},[r("img",{staticClass:"img-fluid mx-auto d-block",attrs:{src:t.showImageList(e.thumbnail),alt:""}})])],1),r("div",{staticClass:"mt-4 text-center"},[r("h5",{staticClass:"mb-3 text-truncate"},[r("router-link",{staticClass:"text-dark",attrs:{to:"/ecommerce/product-detail/"+e.id}},[t._v(t._s(e.descricao))])],1),t._m(2,!0),r("h5",{staticClass:"my-0"},[r("span",{staticClass:"text-muted me-2"},[r("del",[t._v("$"+t._s(t._f("dolar")(e.preco)))])]),r("b",[t._v("$"+t._s(t._f("dolar")(e.preco)))])])])])])])})),0)])]):t._e()])},n=[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"col-xl-4 col-sm-6"},[r("div",{staticClass:"mt-2"},[r("h5",[t._v("Vitrine de produtos")])])])},function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("ul",{staticClass:"nav nav-pills product-view-nav"},[r("li",{staticClass:"nav-item"},[r("a",{staticClass:"nav-link active",attrs:{href:"javascript: void(0);"}},[r("i",{staticClass:"bx bx-grid-alt"})])]),r("li",{staticClass:"nav-item"},[r("a",{staticClass:"nav-link",attrs:{href:"javascript: void(0);"}},[r("i",{staticClass:"bx bx-list-ul"})])])])},function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("p",{staticClass:"text-muted"},[r("i",{staticClass:"bx bxs-star text-warning"}),r("i",{staticClass:"bx bxs-star text-warning"}),r("i",{staticClass:"bx bxs-star text-warning"}),r("i",{staticClass:"bx bxs-star text-warning"}),r("i",{staticClass:"bx bxs-star"})])}],s=(r("a4d3"),r("e01a"),r("4de4"),r("4160"),r("ac1f"),r("841c"),r("2ca0"),r("159b"),r("96cf"),r("1da1")),o=r("c2a4"),i=r("4ab4"),c={page:{title:"Site Infinity",meta:[{name:"description",content:o.description}]},data:function(){return{title:"Site",items:[{text:"Dashboard",href:"/home"},{text:"Site",active:!0}],imgUrl:"",categorias:[],mostrarCategorias:!1,api:new i["a"],subcategoria:{id:0,descricao:""},produtos:{},currentPage:0,termo:""}},created:function(){this.iniciar(),this.listarProdutos()},mounted:function(){this.imgUrl="http://35.247.220.10:8000"},methods:{ativarCategorias:function(){this.mostrarCategorias=!this.mostrarCategorias},iniciar:function(){var t=this;return Object(s["a"])(regeneratorRuntime.mark((function e(){var r,a,n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t.categorias=[],e.next=3,t.api.getCategorias();case 3:return r=e.sent,t.categorias=r,e.next=7,t.api.getSubCategorias();case 7:a=e.sent,n=[],t.categorias.forEach((function(t){n=[],a.forEach((function(e){e.categoria.id==t.id&&n.push(e)})),t.subcategoria=n})),console.log("CATEGORIAS: =>",t.categorias);case 11:case"end":return e.stop()}}),e)})))()},showImageList:function(t){var e="";return e=t?t.startsWith("/media")?this.imgUrl+t:t:this.imgUrl+"media/img/empty.png",e},listarProdutos:function(){var t=this;return Object(s["a"])(regeneratorRuntime.mark((function e(){var r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t.imgUrl="",t.produtos=[],e.next=4,t.api.getProdutos();case 4:r=e.sent,console.log(r),t.produtos=r;case 7:case"end":return e.stop()}}),e)})))()},listarProdutosByCategoria:function(t){var e=this;return Object(s["a"])(regeneratorRuntime.mark((function r(){var a;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return e.imgUrl="http://35.247.220.10:8000",e.produtos=[],console.log("id da categoria a ser buscada",t),r.next=5,e.api.getProdutos();case 5:a=r.sent,console.log(a),e.produtos=a,e.mostrarCategorias=!1;case 9:case"end":return r.stop()}}),r)})))()},listarProdutosBySubCategoria:function(t){var e=this;return Object(s["a"])(regeneratorRuntime.mark((function r(){var a;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return e.imgUrl="http://35.247.220.10:8000",e.produtos=[],console.log("id da sub-categoria a ser buscada",t),r.next=5,e.api.getProdutoBySubcategoria(t);case 5:a=r.sent,console.log(a),e.produtos=a,console.log(e.produtos),e.mostrarCategorias=!1;case 10:case"end":return r.stop()}}),r)})))()},listarProdutosByName:function(){var t=this;return Object(s["a"])(regeneratorRuntime.mark((function e(){var r,a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=t.termo,t.imgUrl="http://35.247.220.10:8000",t.produtos=[],e.next=5,t.api.getProdutoByName(r);case 5:a=e.sent,console.log(a),t.produtos=a,console.log(t.produtos),t.mostrarCategorias=!1;case 10:case"end":return e.stop()}}),e)})))()},searchFilter:function(t){var e=t.target.value,r=this.produtos;this.produtos=r.filter((function(t){return-1!==t.descricao.toLowerCase().search(e.toLowerCase())}))},irHome:function(){this.$router.push("/home")}}},u=c,l=(r("4d5f"),r("2877")),p=Object(l["a"])(u,a,n,!1,null,null,null);e["default"]=p.exports},"45eb":function(t,e,r){"use strict";r.d(e,"a",(function(){return s}));r("e439"),r("5d41");var a=r("7e84");function n(t,e){while(!Object.prototype.hasOwnProperty.call(t,e))if(t=Object(a["a"])(t),null===t)break;return t}function s(t,e,r){return s="undefined"!==typeof Reflect&&Reflect.get?Reflect.get:function(t,e,r){var a=n(t,e);if(a){var s=Object.getOwnPropertyDescriptor(a,e);return s.get?s.get.call(r):s.value}},s(t,e,r||t)}},"4ab4":function(t,e,r){"use strict";r.d(e,"a",(function(){return p}));r("96cf");var a=r("1da1"),n=r("d4ec"),s=r("bee2"),o=r("45eb"),i=r("7e84"),c=r("262e"),u=r("2caf"),l=r("b7dc"),p=function(t){Object(c["a"])(r,t);var e=Object(u["a"])(r);function r(){return Object(n["a"])(this,r),e.call(this)}return Object(s["a"])(r,[{key:"getCategorias",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){var e,a=arguments;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e=a.length>0&&void 0!==a[0]?a[0]:-1,t.next=3,Object(o["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"categoria",e);case 3:return t.abrupt("return",t.sent);case 4:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"saveCategoria",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"categoria",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"delCategoria",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"categoria",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"getSubCategorias",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){var e,a=arguments;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e=a.length>0&&void 0!==a[0]?a[0]:-1,t.next=3,Object(o["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"subcategoria",e);case 3:return t.abrupt("return",t.sent);case 4:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"saveSubCategoria",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"subcategoria",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"delSubCategoria",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"subcategoria",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"getProdutos",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){var e,a=arguments;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e=a.length>0&&void 0!==a[0]?a[0]:-1,t.next=3,Object(o["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"produto",e);case 3:return t.abrupt("return",t.sent);case 4:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"getProdutoByName",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"produto/by-descricao",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"getProdutoBySubcategoria",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"produto/by-subcategoria",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"saveProduto",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"produto",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"delProduto",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"produto",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"getEmpresas",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){var e,a=arguments;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e=a.length>0&&void 0!==a[0]?a[0]:-1,t.next=3,Object(o["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"empresa",e);case 3:return t.abrupt("return",t.sent);case 4:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"saveEmpresa",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"empresa",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"delEmpresa",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"empresa",e);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()}]),r}(l["a"])},"4d5f":function(t,e,r){"use strict";r("9c73")},"5d41":function(t,e,r){var a=r("23e7"),n=r("861d"),s=r("825a"),o=r("5135"),i=r("06cf"),c=r("e163");function u(t,e){var r,a,l=arguments.length<3?t:arguments[2];return s(t)===l?t[e]:(r=i.f(t,e))?o(r,"value")?r.value:void 0===r.get?void 0:r.get.call(l):n(a=c(t))?u(a,e,l):void 0}a({target:"Reflect",stat:!0},{get:u})},"5eef":function(t,e,r){"use strict";r.d(e,"a",(function(){return i}));r("d3b7"),r("ac1f"),r("25f0"),r("1276"),r("96cf");var a=r("1da1"),n=r("d4ec"),s=r("bee2"),o=r("ade3"),i=function(){function t(){Object(n["a"])(this,t),Object(o["a"])(this,"decodeToken",(function(t){try{return JSON.parse(atob(t.split(".")[1]))}catch(e){return null}})),this.SERVER_URL="http://35.247.220.10:8000/rest/v1/",this.TOKEN_URL=this.SERVER_URL+"token/",this.REFRESH_URL=this.TOKEN_URL+"refresh/",this.credenciais=""}return Object(s["a"])(t,[{key:"login",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e,r){var a,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return this.credenciais={username:e,password:r},a=null,t.prev=2,t.next=5,fetch(this.TOKEN_URL,{method:"POST",body:JSON.stringify(this.credenciais),mode:"cors",headers:{"Content-Type":"application/json"}});case 5:return n=t.sent,t.next=8,n.json();case 8:a=t.sent,t.next=14;break;case 11:t.prev=11,t.t0=t["catch"](2),a={error:t.t0.toString()};case 14:return t.abrupt("return",a);case 15:case"end":return t.stop()}}),t,this,[[2,11]])})));function e(e,r){return t.apply(this,arguments)}return e}()},{key:"getToken",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(){var e,r,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(e=localStorage.getItem("access"),r=localStorage.getItem("refresh"),a="",!this.tokenExpired(e)){t.next=14;break}return t.prev=4,t.next=7,this.refreshToken(r);case 7:a=t.sent,t.next=13;break;case 10:return t.prev=10,t.t0=t["catch"](4),t.abrupt("return",t.t0.toString());case 13:null==a?(localStorage.removeItem("access"),localStorage.removeItem("refresh"),e=null):(e=a.access,localStorage.setItem("access",e));case 14:return a={access:e,refresh:r},t.abrupt("return",a);case 16:case"end":return t.stop()}}),t,this,[[4,10]])})));function e(){return t.apply(this,arguments)}return e}()},{key:"tokenExpired",value:function(t){t=this.decodeToken(t);var e=!1;if(null!=t){var r=Date.now()/1e3;t.exp<r&&(e=!0)}else e=!0;return e}},{key:"refreshToken",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){var r,a,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return console.log("entrou no refreshtoken do auth"),r={refresh:e},a=null,t.prev=3,console.log("try"),t.next=7,fetch(this.REFRESH_URL,{method:"POST",body:JSON.stringify(r),mode:"cors",headers:{"Content-Type":"application/json"}});case 7:if(n=t.sent,200===n.status){t.next=10;break}throw new Error("ERRO DO SILVIAO");case 10:return t.next=12,n.json();case 12:a=t.sent,t.next=20;break;case 15:return t.prev=15,t.t0=t["catch"](3),console.log(t.t0),a=null,t.abrupt("return",!1);case 20:return console.log("zzz"),t.abrupt("return",a);case 22:case"end":return t.stop()}}),t,this,[[3,15]])})));function e(e){return t.apply(this,arguments)}return e}()}]),t}()},"9c73":function(t,e,r){},b7dc:function(t,e,r){"use strict";r.d(e,"a",(function(){return p}));r("d3b7"),r("25f0");var a=r("53ca"),n=(r("96cf"),r("1da1")),s=r("d4ec"),o=r("bee2"),i=r("bc3a"),c=r.n(i),u=r("5eef"),l=new u["a"],p=function(){function t(){Object(s["a"])(this,t),this.SERVER_URL="http://35.247.220.10:8000/rest/v1/",this.IMG_URL="http://35.247.220.10:8000",this.TOKEN_URL=this.SERVER_URL+"token/",this.USUARIO="conejofoz",this.PASSWORD="1234567.",this.credenciais={username:this.USUARIO,password:this.PASSWORD}}return Object(o["a"])(t,[{key:"getToken_old",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(){var e,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,fetch(this.TOKEN_URL,{method:"POST",body:JSON.stringify(this.credenciais),mode:"cors",headers:{"Content-Type":"application/json"}});case 2:return e=t.sent,t.next=5,e.json();case 5:return r=t.sent,t.abrupt("return",r);case 7:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"getToken",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(){var e;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return console.log("entrou no get token da api"),t.prev=1,t.next=4,l.getToken();case 4:if(e=t.sent,console.log("get token da api",e),!e.detail){t.next=9;break}return console.log("get token da api entrou no if",e),t.abrupt("return",e.detail);case 9:return console.log("get token da api passou do if",e),t.abrupt("return",e);case 13:return t.prev=13,t.t0=t["catch"](1),console.log("error no get token da api ",t.t0),t.abrupt("return",t.t0.toString());case 17:case"end":return t.stop()}}),t,null,[[1,13]])})));function e(){return t.apply(this,arguments)}return e}()},{key:"get",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(e){var r,a,n,s,o,i,c,u,l=arguments;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return r=l.length>1&&void 0!==l[1]?l[1]:-1,a=l.length>2&&void 0!==l[2]?l[2]:"",n=l.length>3&&void 0!==l[3]?l[3]:"",s=l.length>4&&void 0!==l[4]?l[4]:"",t.prev=4,t.next=7,this.getToken();case 7:return o=t.sent,console.log(o),i=this.SERVER_URL+e+"/",-1!==r?i+=r+"/":a>""?i+=""==s?"?dataInicial="+a+"&dataFinal="+n:"?dataInicial="+a+"&dataFinal="+n+"&empresa="+s:""==!s&&(i+="?empresa="+s),t.next=13,fetch(i,{method:"GET",headers:{"Content-Type":"application/json",Authorization:"Bearer "+o.access}});case 13:if(c=t.sent,console.log(c.status),404!=c.status){t.next=17;break}throw new Error("404");case 17:return c?console.log("tem resposta na api"):console.log("não tem resposta na api"),console.log("resposta api: ",c),t.next=21,c.json();case 21:if(u=t.sent,console.log("itens na api principal: ",u),void 0!==u.results){t.next=25;break}return t.abrupt("return",u);case 25:return t.abrupt("return",u.results);case 28:return t.prev=28,t.t0=t["catch"](4),console.log("Erro no get da api",t.t0.toString()),t.abrupt("return",t.t0.message);case 32:case"end":return t.stop()}}),t,this,[[4,28]])})));function e(e){return t.apply(this,arguments)}return e}()},{key:"saveNormalSemFotoApi",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(e,r){var a,n,s,o,i;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,this.getToken();case 2:return a=t.sent,n=this.SERVER_URL+e+"/",s="POST",-1!==r.id&&(s="PUT",n+=r.id+"/"),t.prev=6,t.next=9,fetch(n,{method:s,body:JSON.stringify(r),headers:{"Content-Type":"application/json",Authorization:"Bearer "+a.access}});case 9:if(o=t.sent,console.log("resposta pura: ",o),o.ok){t.next=14;break}return console.log("resposta do if: ",o.statusText),t.abrupt("return",o.statusText);case 14:return t.next=16,o.json();case 16:return i=t.sent,console.log("data: ",i),t.abrupt("return",i);case 21:t.prev=21,t.t0=t["catch"](6),console.log(t.t0);case 24:case"end":return t.stop()}}),t,this,[[6,21]])})));function e(e,r){return t.apply(this,arguments)}return e}()},{key:"save",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(e,r){var n,s,o;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return console.log("Objeto antes de gravar: ",r),console.log("Valor do id: ",r.get("id")),t.next=4,this.getToken();case 4:if(n=t.sent,s=this.SERVER_URL+e+"/",-1!=r.get("id")&&(s+=r.get("id")+"/"),t.prev=7,o=null,-1!=r.get("id")){t.next=15;break}return t.next=12,c.a.post(s,r,{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+n.access}},{onUploadProgress:function(t){console.log("Upload Progress: "+Math.round(t.loaded/t.total*100)+"%")}}).then((function(t){return console.log("res",t),t}));case 12:o=t.sent,t.next=18;break;case 15:return t.next=17,c.a.put(s,r,{headers:{"Content-Type":"multipart/form-data",Authorization:"Bearer "+n.access}},{onUploadProgress:function(t){console.log("Upload Progress: "+Math.round(t.loaded/t.total*100)+"%")}}).then((function(t){return console.log("res",t),t}));case 17:o=t.sent;case 18:if(console.log("resposta pura: ",o),console.log("tipo da resposta pura :",Object(a["a"])(o)),console.log("resposta pura convertida para json :",JSON.stringify(o)),console.log("resposta mensagem :",o.message),console.log("resposta config :",o.config),!o.data){t.next=28;break}return console.log("existe data"),t.abrupt("return",o.data);case 28:return console.log("nao existe data"),t.abrupt("return",o.message);case 30:t.next=41;break;case 32:return t.prev=32,t.t0=t["catch"](7),console.log("======================TRAYY============================="),console.log("Erro retornado do tray: ",t.t0),console.log("tipo do erro retornado do tray: ",Object(a["a"])(t.t0)),console.log("ERRO do tray PARA JSON: ",JSON.stringify(t.t0)),console.log("ERRO do tray response: ",t.t0.response),console.log("ERRO do tray response: ",JSON.stringify(t.t0.response.data)),t.abrupt("return",JSON.stringify(t.t0.response.data));case 41:case"end":return t.stop()}}),t,this,[[7,32]])})));function e(e,r){return t.apply(this,arguments)}return e}()},{key:"delete",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(e,r){var n,s,o;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,this.getToken();case 2:return n=t.sent,s=this.SERVER_URL+e+"/"+r+"/",t.prev=4,t.next=7,fetch(s,{method:"DELETE",headers:{"Content-Type":"application/json",Authorization:"Bearer "+n.access}}).catch((function(t){return console.log("Error: ",t)}));case 7:return o=t.sent,console.log("passou"),console.log(o),console.log("resposta pura: ",o),console.log("tipo da resposta pura :",Object(a["a"])(o)),console.log("resposta pura convertida para json :",JSON.stringify(o)),console.log("resposta mensagem :",o.message),console.log("resposta config :",o.config),console.log("resposta data :",o.data),t.abrupt("return",o);case 19:return t.prev=19,t.t0=t["catch"](4),console.log(t.t0),t.abrupt("return",t.t0);case 23:case"end":return t.stop()}}),t,this,[[4,19]])})));function e(e,r){return t.apply(this,arguments)}return e}()}]),t}()}}]);
//# sourceMappingURL=chunk-5d2ba070.02a16773.js.map