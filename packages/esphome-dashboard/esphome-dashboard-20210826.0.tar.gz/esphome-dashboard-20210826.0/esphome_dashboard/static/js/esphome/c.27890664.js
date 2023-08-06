import{i as o,_ as e,w as t,r as n,n as i,h as s,T as a}from"./c.2c9aeedd.js";import"./c.d32d4248.js";import{a as c}from"./c.04e11fe1.js";import"./index-aa9e8c11.js";import"./c.d1723f10.js";import"./c.38391347.js";import"./c.8551ca08.js";let r=class extends s{render(){return a`
      <esphome-process-dialog
        .heading=${`Download ${this.configuration}`}
        .type=${"compile"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
        @process-done=${this._handleProcessDone}
      >
        ${void 0===this._result?"":0===this._result?a`
              <a
                slot="secondaryAction"
                href="${`./download.bin?configuration=${encodeURIComponent(this.configuration)}`}"
              >
                <mwc-button label="Download"></mwc-button>
              </a>
            `:a`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Retry"
                @click=${this._handleRetry}
              ></mwc-button>
            `}
      </esphome-process-dialog>
    `}_handleProcessDone(o){if(this._result=o.detail,0!==o.detail)return;const e=document.createElement("a");e.download=this.configuration+".bin",e.href=`./download.bin?configuration=${encodeURIComponent(this.configuration)}`,document.body.appendChild(e),e.click(),e.remove()}_handleRetry(){c(this.configuration)}_handleClose(){this.parentNode.removeChild(this)}};r.styles=o`
    a {
      text-decoration: none;
    }
  `,e([t()],r.prototype,"configuration",void 0),e([n()],r.prototype,"_result",void 0),r=e([i("esphome-compile-dialog")],r);
