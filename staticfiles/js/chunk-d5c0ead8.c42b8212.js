(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-d5c0ead8"],{"0afc":function(e,t,r){"use strict";r.r(t);var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("Layout",[r("PageHeader",{attrs:{title:e.title,items:e.items}}),r("v-col",[r("v-row",[r("v-col",{attrs:{cols:"12",md:"3"}},[r("v-card",[r("v-card-title",[e._v("Clientes")]),r("v-card-text",[r("h1",[e._v(e._s(e.totalClientes))])])],1)],1),r("v-col",{attrs:{cols:"12",md:"3"}},[r("v-card",[r("v-card-title",[e._v("Produtos")]),r("v-card-text",[r("h1",[e._v(e._s(e.totalProdutos))])])],1)],1)],1)],1)],1)},a=[],c=(r("a4d3"),r("e01a"),r("96cf"),r("1da1")),u=r("444f"),i=r("c2a4"),s=r("2579"),o=r("5eef"),l=r("0c73"),p=r("4ab4"),h={page:{title:"Dashboard",meta:[{name:"description",content:i.description}]},components:{Layout:u["a"],PageHeader:s["a"]},data:function(){return{apiAuth:new o["a"],apiFac:new l["a"],apiInv:new p["a"],totalClientes:0,totalProdutos:0,title:"Dashboard",items:[{text:"Dashboards",href:"/"},{text:"Default",active:!0}],statData:[{icon:"bx bx-copy-alt",title:"Orders",value:"1,235"},{icon:"bx bx-archive-in",title:"Revenue",value:"$35, 723"},{icon:"bx bx-purchase-tag-alt",title:"Average Price",value:"$16.2"}],transactions:[{id:"#SK2540",name:"Neal Matthews",date:"07 Oct, 2019",total:"$400",status:"Paid",payment:["fa-cc-mastercard","Mastercard"],index:1},{id:"#SK2541",name:"Jamal Burnett",date:"07 Oct, 2019",total:"$380",status:"Chargeback",payment:["fa-cc-visa","Visa"],index:2},{id:"#SK2542",name:"Juan Mitchell",date:"06 Oct, 2019",total:"$384",status:"Paid",payment:["fab fa-cc-paypal","Paypal"],index:3},{id:"#SK2543",name:"Barry Dick",date:"05 Oct, 2019",total:"$412",status:"Paid",payment:["fa-cc-mastercard","Mastercard"],index:4},{id:"#SK2544",name:"Ronald Taylor",date:"04 Oct, 2019",total:"$404",status:"Refund",payment:["fa-cc-visa","Visa"],index:5},{id:"#SK2545",name:"Jacob Hunter",date:"04 Oct, 2019",total:"$392",status:"Paid",payment:["fab fa-cc-paypal","Paypal"],index:6}],showModal:!1,isLoading:!1,fullPage:!0,canCancel:!1,useSlot:!1,loader:"spinner",color:"#007bff",bgColor:"#ffffff",height:128,width:128,timeout:3e3,fetchingStats:!0,earningStatus:!0}},created:function(){this.verificaAcesso()},mounted:function(){var e=this;setTimeout((function(){e.showModal=!0}),1500)},methods:{verificaAcesso:function(){var e=this;return Object(c["a"])(regeneratorRuntime.mark((function t(){var r,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return console.log("entrou no verifica acesso"),t.prev=1,t.next=4,e.apiFac.getCliente(-1);case 4:return r=t.sent,console.log("clientes: ",r),r.detail&&(console.log("foi pro login"),e.$router.push("/login")),console.log(r),e.totalClientes=r.length,t.next=11,e.apiInv.getProdutos(-1);case 11:n=t.sent,e.totalProdutos=n.length,t.next=18;break;case 15:t.prev=15,t.t0=t["catch"](1),e.mensagemErro(t.t0);case 18:case"end":return t.stop()}}),t,null,[[1,15]])})))()}}},f=h,d=r("2877"),v=r("6544"),b=r.n(v),g=r("b0af"),m=r("99d9"),y=r("62ad"),w=r("0fd9"),O=Object(d["a"])(f,n,a,!1,null,null,null);t["default"]=O.exports;b()(O,{VCard:g["a"],VCardText:m["b"],VCardTitle:m["c"],VCol:y["a"],VRow:w["a"]})},"0c73":function(e,t,r){"use strict";r.d(t,"a",(function(){return d}));r("96cf");var n=r("1da1"),a=r("d4ec"),c=r("bee2"),u=r("45eb"),i=r("7e84"),s=r("262e"),o=r("2caf"),l=r("b7dc"),p="cliente",h="vendas-detalhe",f="vendas",d=function(e){Object(s["a"])(r,e);var t=Object(o["a"])(r);function r(){return Object(a["a"])(this,r),t.call(this)}return Object(c["a"])(r,[{key:"getCliente",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=n.length>0&&void 0!==n[0]?n[0]:-1,e.next=3,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,p,t);case 3:return e.abrupt("return",e.sent);case 4:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"saveCliente",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"save",this).call(this,p,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"deleteCliente",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,p,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getVenda",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n,a,c,s=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=s.length>0&&void 0!==s[0]?s[0]:-1,n=s.length>1&&void 0!==s[1]?s[1]:"",a=s.length>2&&void 0!==s[2]?s[2]:"",c=s.length>3&&void 0!==s[3]?s[3]:"",e.next=6,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,f,t,n,a,c);case 6:return e.abrupt("return",e.sent);case 7:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"saveVenda",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"save",this).call(this,f,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"saveDetalheVenda",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"save",this).call(this,h,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"deleteDetalhe",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,h,t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getClienteByName",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"cliente/by-name",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getProdutoByName",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"produto/by-descricao",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getProdutos",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"produto",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()}]),r}(l["a"])},"4ab4":function(e,t,r){"use strict";r.d(t,"a",(function(){return p}));r("96cf");var n=r("1da1"),a=r("d4ec"),c=r("bee2"),u=r("45eb"),i=r("7e84"),s=r("262e"),o=r("2caf"),l=r("b7dc"),p=function(e){Object(s["a"])(r,e);var t=Object(o["a"])(r);function r(){return Object(a["a"])(this,r),t.call(this)}return Object(c["a"])(r,[{key:"getCategorias",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=n.length>0&&void 0!==n[0]?n[0]:-1,e.next=3,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"categoria",t);case 3:return e.abrupt("return",e.sent);case 4:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"saveCategoria",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"categoria",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"delCategoria",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"categoria",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getSubCategorias",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=n.length>0&&void 0!==n[0]?n[0]:-1,e.next=3,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"subcategoria",t);case 3:return e.abrupt("return",e.sent);case 4:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"saveSubCategoria",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"subcategoria",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"delSubCategoria",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"subcategoria",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getProdutos",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=n.length>0&&void 0!==n[0]?n[0]:-1,e.next=3,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"produto",t);case 3:return e.abrupt("return",e.sent);case 4:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"getProdutoByName",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"produto/by-descricao",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"saveProduto",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"produto",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"delProduto",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"produto",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"getEmpresas",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(){var t,n=arguments;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t=n.length>0&&void 0!==n[0]?n[0]:-1,e.next=3,Object(u["a"])(Object(i["a"])(r.prototype),"get",this).call(this,"empresa",t);case 3:return e.abrupt("return",e.sent);case 4:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"saveEmpresa",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"save",this).call(this,"empresa",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()},{key:"delEmpresa",value:function(){var e=Object(n["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,Object(u["a"])(Object(i["a"])(r.prototype),"delete",this).call(this,"empresa",t);case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}()}]),r}(l["a"])}}]);
//# sourceMappingURL=chunk-d5c0ead8.c42b8212.js.map