(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-521d57db"],{"0c73":function(e,t,r){"use strict";r.d(t,"a",(function(){return f}));r("96cf");var n=r("1da1"),a=r("d4ec"),i=r("bee2"),c=r("45eb"),s=r("7e84"),o=r("262e"),u=r("2caf"),l=r("b7dc"),d="cliente",p="vendas-detalhe",v="vendas",f=function(e){Object(o["a"])(r,e);var t=Object(u["a"])(r);function r(){return Object(a["a"])(this,r),t.call(this)}return Object(i["a"])(r,[{key:"getCliente",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=n.length>0&&void 0!==n[0]?n[0]:-1,e.next=3,Object(c["a"])(Object(s["a"])(r.prototype),"get",this).call(this,d,t);case 3:return e.abrupt("return",e.sent);case 4:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"saveCliente",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"save",this).call(this,d,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"deleteCliente",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"delete",this).call(this,d,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getVenda",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n,a,i,o=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=o.length>0&&void 0!==o[0]?o[0]:-1,n=o.length>1&&void 0!==o[1]?o[1]:"",a=o.length>2&&void 0!==o[2]?o[2]:"",i=o.length>3&&void 0!==o[3]?o[3]:"",e.next=6,Object(c["a"])(Object(s["a"])(r.prototype),"get",this).call(this,v,t,n,a,i);case 6:return e.abrupt("return",e.sent);case 7:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"saveVenda",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"save",this).call(this,v,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"saveDetalheVenda",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"save",this).call(this,p,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"deleteDetalhe",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"delete",this).call(this,p,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getClienteByName",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"get",this).call(this,"cliente/by-name",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getProdutoByName",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"get",this).call(this,"produto/by-descricao",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getProdutos",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(c["a"])(Object(s["a"])(r.prototype),"get",this).call(this,"produto",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()}]),r}(l["a"])},2546:function(e,t,r){"use strict";r.r(t);var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("Layout",[r("PageHeader",{attrs:{title:e.title,items:e.items}}),r("v-app",[r("v-row",[r("v-col",[r("v-text-field",{attrs:{"append-icon":"mdi-magnify",label:"Buscar"},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}}),r("v-data-table",{staticClass:"elevation-1",attrs:{dense:"",headers:e.headers,items:e.itens,search:e.search,loading:e.loading,"loading-text":"Carregando..."},scopedSlots:e._u([{key:"top",fn:function(){return[r("v-toolbar",{attrs:{flat:"",color:"white"}},[r("v-toolbar-title",[e._v("Vendas")]),r("v-divider",{staticClass:"mx-4",attrs:{inset:"",vertical:""}}),r("v-spacer"),r("v-btn",{staticClass:"mb-2",attrs:{color:"warning",dark:""},on:{click:e.iniciar}},[r("v-icon",[e._v("cached")])],1),r("v-btn",{staticClass:"mb-2",attrs:{color:"success",dark:""},on:{click:e.novaVenda}},[r("v-icon",[e._v("add_box")])],1),r("v-dialog",{attrs:{"max-width":"500px"},scopedSlots:e._u([{key:"activator",fn:function(t){var n=t.on,a=t.attrs;return[r("v-btn",e._g(e._b({staticClass:"mb-2",attrs:{color:"primary",dark:""}},"v-btn",a,!1),n),[r("v-icon",[e._v("add_box")])],1)]}}]),model:{value:e.dialog,callback:function(t){e.dialog=t},expression:"dialog"}},[r("v-card",[r("v-card-title",[r("span",{staticClass:"headline"},[e._v(e._s(e.formTitle))])]),r("v-card-text",[r("v-container",[r("v-row",[r("v-col",{attrs:{cols:"2",sm:"2",md:"2"}},[r("v-text-field",{attrs:{label:"ID",disabled:""},model:{value:e.editedItem.id,callback:function(t){e.$set(e.editedItem,"id",t)},expression:"editedItem.id"}})],1),r("v-col",{attrs:{cols:"10",sm:"10",md:"10"}},[r("v-text-field",{attrs:{label:"Descrição"},model:{value:e.editedItem.descricao,callback:function(t){e.$set(e.editedItem,"descricao",t)},expression:"editedItem.descricao"}})],1)],1)],1)],1),r("v-card-actions",[r("v-spacer"),r("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:e.close}},[e._v("Cancelar")]),r("v-btn",{attrs:{color:"pink accent-3",text:""},on:{click:e.save}},[e._v("Salvar")])],1)],1)],1)],1)]},proxy:!0},{key:"item.acoes",fn:function(t){var n=t.item;return[r("v-icon",{staticClass:"mr-2",attrs:{small:""},on:{click:function(t){return e.editItem(n)}}},[e._v("mdi-pencil")]),r("v-icon",{attrs:{small:"",color:"danger"},on:{click:function(t){return e.deleteItem(n)}}},[e._v("mdi-delete")])]}},{key:"no-data",fn:function(){return[r("v-btn",{attrs:{color:"primary"},on:{click:e.iniciar}},[e._v("Reiniciar")])]},proxy:!0}])})],1)],1)],1)],1)},a=[],i=(r("c975"),r("96cf"),r("1da1")),c=r("444f"),s=r("2579"),o=r("0c73"),u=r("c077"),l={name:"Vendas",components:{Layout:c["a"],PageHeader:s["a"]},props:[],mixins:[u["a"]],data:function(){return{title:"Vendas",items:[{text:"Dashboard",href:"/home"},{text:"Vendas",active:!0}],itens:[],api:new o["a"],loading:!1,search:"",headers:[{text:"ID",value:"id"},{text:"Data",align:"start",sortable:!1,value:"data"},{text:"Cliente",align:"start",sortable:!1,value:"cliente.nome"},{text:"Empresa",align:"start",sortable:!1,value:"empresa"},{text:"Ações",value:"acoes",sortable:!1}],dialog:!1,editedIndex:-1,editedItem:{id:-1,descricao:""},defaultItem:{id:-1,descricao:""}}},created:function(){this.iniciar()},methods:{iniciar:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){var r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.prev=0,e.loading=!0,t.next=4,e.api.getVenda();case 4:r=t.sent,e.itens=r,t.next=11;break;case 8:t.prev=8,t.t0=t["catch"](0),e.mensagemErro(t.t0);case 11:return t.prev=11,e.loading=!1,t.finish(11);case 14:case"end":return t.stop()}}),t,null,[[0,8,11,14]])})))()},novaVenda:function(){this.$router.push("/venda")},close:function(){var e=this;this.dialog=!1,this.$nextTick((function(){e.editedItem=Object.assign({},e.defaultItem),e.editedIndex=-1}))},editItem:function(e){this.editedIndex=this.itens.indexOf(e),this.editedItem=Object.assign({},e),this.dialog=!0},deleteItem:function(e){var t=this;return Object(i["a"])(regeneratorRuntime.mark((function r(){return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return r.next=2,t.mensagemPergunta("venda ".concat(e.descricao,"?"),"Apagar");case 2:if(!r.sent){r.next=7;break}return r.next=5,t.api.delCategoria(e.id);case 5:t.iniciar(),t.mensagem("eliminada com sucesso!","Venda");case 7:case"end":return r.stop()}}),r)})))()},save:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){var r,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:for(n in r=new FormData,e.editedItem)r.append(n,e.editedItem[n]);return t.prev=2,e.loading=!0,t.next=6,e.api.saveCategoria(r);case 6:e.close(),e.iniciar(),e.mensagem("Salvo com sucesso","salvo","success"),t.next=14;break;case 11:t.prev=11,t.t0=t["catch"](2),alert(t.t0);case 14:return t.prev=14,e.loading=!1,t.finish(14);case 17:case"end":return t.stop()}}),t,null,[[2,11,14,17]])})))()}},computed:{formTitle:function(){return(-1===this.editedIndex?"Nova ":"Editar ")+"Categoria"}},watch:{dialog:function(e){e||this.close()}}},d=l,p=r("2877"),v=r("6544"),f=r.n(v),m=r("7496"),h=r("8336"),b=r("b0af"),g=r("99d9"),x=r("62ad"),w=r("a523"),k=r("8fea"),y=r("169a"),O=r("ce7e"),j=r("132d"),C=r("0fd9"),R=r("2fa4"),V=r("8654"),I=r("71d9"),_=r("2a7f"),T=Object(p["a"])(d,n,a,!1,null,null,null);t["default"]=T.exports;f()(T,{VApp:m["a"],VBtn:h["a"],VCard:b["a"],VCardActions:g["a"],VCardText:g["b"],VCardTitle:g["c"],VCol:x["a"],VContainer:w["a"],VDataTable:k["a"],VDialog:y["a"],VDivider:O["a"],VIcon:j["a"],VRow:C["a"],VSpacer:R["a"],VTextField:V["a"],VToolbar:I["a"],VToolbarTitle:_["a"]})},a523:function(e,t,r){"use strict";r("99af"),r("4de4"),r("b64b"),r("2ca0"),r("20f6"),r("4b85"),r("a15b"),r("498a");var n=r("2b0e");function a(e){return n["default"].extend({name:"v-".concat(e),functional:!0,props:{id:String,tag:{type:String,default:"div"}},render:function(t,r){var n=r.props,a=r.data,i=r.children;a.staticClass="".concat(e," ").concat(a.staticClass||"").trim();var c=a.attrs;if(c){a.attrs={};var s=Object.keys(c).filter((function(e){if("slot"===e)return!1;var t=c[e];return e.startsWith("data-")?(a.attrs[e]=t,!1):t||"string"===typeof t}));s.length&&(a.staticClass+=" ".concat(s.join(" ")))}return n.id&&(a.domProps=a.domProps||{},a.domProps.id=n.id),t(n.tag,a,i)}})}var i=r("d9f7");t["a"]=a("container").extend({name:"v-container",functional:!0,props:{id:String,tag:{type:String,default:"div"},fluid:{type:Boolean,default:!1}},render:function(e,t){var r,n=t.props,a=t.data,c=t.children,s=a.attrs;return s&&(a.attrs={},r=Object.keys(s).filter((function(e){if("slot"===e)return!1;var t=s[e];return e.startsWith("data-")?(a.attrs[e]=t,!1):t||"string"===typeof t}))),n.id&&(a.domProps=a.domProps||{},a.domProps.id=n.id),e(n.tag,Object(i["a"])(a,{staticClass:"container",class:Array({"container--fluid":n.fluid}).concat(r||[])}),c)}})},c077:function(e,t,r){"use strict";r("96cf");var n=r("1da1");t["a"]={methods:{mensagem:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"",r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"success";this.$swal({title:t,text:e,icon:r,allowOutsideClick:!1,confirmButtonText:"Ok"})},mensagemPergunta:function(e,t){var r=arguments,a=this;return Object(n["a"])(regeneratorRuntime.mark((function n(){var i,c;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return i=r.length>2&&void 0!==r[2]?r[2]:"question",n.prev=1,n.next=4,a.$swal({title:t,text:e,icon:i,showCancelButton:!0,confirmButtonText:"Sim",cancelButtonText:"Não",reverseButtons:!0});case 4:return c=n.sent,n.abrupt("return",c.isConfirmed);case 8:n.prev=8,n.t0=n["catch"](1);case 10:case"end":return n.stop()}}),n,null,[[1,8]])})))()}}}}}]);
//# sourceMappingURL=chunk-521d57db.b66d10ea.js.map