(self.webpackChunkwebgui_jupyter_widgets=self.webpackChunkwebgui_jupyter_widgets||[]).push([[568],{568:function(e,i,t){"use strict";var n=this&&this.__createBinding||(Object.create?function(e,i,t,n){void 0===n&&(n=t),Object.defineProperty(e,n,{enumerable:!0,get:function(){return i[t]}})}:function(e,i,t,n){void 0===n&&(n=t),e[n]=i[t]}),s=this&&this.__exportStar||function(e,i){for(var t in e)"default"===t||Object.prototype.hasOwnProperty.call(i,t)||n(i,e,t)};Object.defineProperty(i,"__esModule",{value:!0}),s(t(657),i),s(t(367),i)},657:(e,i,t)=>{"use strict";Object.defineProperty(i,"__esModule",{value:!0}),i.MODULE_NAME=i.MODULE_VERSION=void 0;const n=t(306);i.MODULE_VERSION=n.version,i.MODULE_NAME=n.name},367:(e,i,t)=>{"use strict";Object.defineProperty(i,"__esModule",{value:!0}),i.WebguiDocuView=i.WebguiView=i.WebguiModel=void 0;const n=t(565),s=t(242),l=t(657);t(204);class r extends n.DOMWidgetModel{defaults(){return Object.assign(Object.assign({},super.defaults()),{_model_name:r.model_name,_model_module:r.model_module,_model_module_version:r.model_module_version,_view_name:r.view_name,_view_module:r.view_module,_view_module_version:r.view_module_version,value:{}})}}i.WebguiModel=r,r.serializers=Object.assign({},n.DOMWidgetModel.serializers),r.model_name="WebguiModel",r.model_module=l.MODULE_NAME,r.model_module_version=l.MODULE_VERSION,r.view_name="WebguiView",r.view_module=l.MODULE_NAME,r.view_module_version=l.MODULE_VERSION;class a extends n.DOMWidgetView{render(){this.el.classList.add("webgui-widget");let e=this.model.get("value");this.scene=new s.Scene;let i=document.createElement("div");i.setAttribute("style","height: 50vw; width: 100vw;"),this.el.appendChild(i),setTimeout((()=>{this.scene.init(i,e),this.scene.render()}),0),this.model.on("change:value",this.value_changed,this)}value_changed(){let e=this.model.get("value");this.scene.updateRenderData(e)}}i.WebguiView=a;class d extends n.DOMWidgetView{render(){const e=this.model.get("value").preview;this.container=$(`\n      <div class="webgui_container" style="width:100%">\n          <img src="${e}" class="image">\n          <div class="webgui_overlay webgui_tooltip">\n              <span class="webgui_tooltiptext"> Click to load interactive WebGUI </span>\n          </div>\n      </div>`);let i=document.createElement("div");this.container.click((e=>this.onClickImage(e))),this.container.appendTo(i),this.el.appendChild(i),this.model.on("change:value",this.data_changed,this)}onClickImage(e){document.body.style.cursor="wait";let i=this.model.get("value");$.get(i.render_data,(e=>{this.container.remove(),this.container=null,document.body.style.cursor="";let i=this.el.children[0];i.innerHTML="",(new s.Scene).init(i,e)}))}data_changed(){let e=this.model.get("value");this.scene.updateRenderData(e)}}i.WebguiDocuView=d},889:(e,i,t)=>{(i=t(645)(!1)).push([e.id,".webgui-widget {\n  padding: 0px 2px;\n}\n",""]),e.exports=i},204:(e,i,t)=>{var n=t(379),s=t(889);"string"==typeof(s=s.__esModule?s.default:s)&&(s=[[e.id,s,""]]);n(s,{insert:"head",singleton:!1}),e.exports=s.locals||{}},306:e=>{"use strict";e.exports=JSON.parse('{"name":"webgui_jupyter_widgets","version":"0.1.4","description":"Jupyter widgetds library for webgui js visualization library\'","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/CERBSim/webgui_jupyter_widgets","bugs":{"url":"https://github.com/CERBSim/webgui_jupyter_widgets/issues"},"license":"LGPL-2.1-or-later","author":{"name":"CERBSim","email":"mhochsteger@cerbsim.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/CERBSim/webgui_jupyter_widgets"},"scripts":{"build":"npm run build:lib && npm run build:nbextension && npm run build:labextension:dev","build:prod":"npm run build:lib && npm run build:nbextension && npm run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"npm run clean:lib && npm run clean:nbextension && npm run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf webgui_jupyter_widgets/labextension","clean:nbextension":"rimraf webgui_jupyter_widgets/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"npm run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch"},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2.0.0 || ^3.0.0 || ^4.0.0"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyterlab/builder":"^3.0.0","@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webgui":"file:webgui","webpack":"^5.30.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"webgui_jupyter_widgets/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}')}}]);