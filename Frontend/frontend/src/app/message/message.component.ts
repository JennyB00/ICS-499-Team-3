import { Component } from '@angular/core';

@Component({
  selector: 'app-message',
  template: `
    <p>
      message works!
      {{ rand }}
    </p>
  `,
  styles: [
  ]
})
export class MessageComponent {
    rand = Math.random();
    constructor() {
      setInterval(() => this.rand = Math.random(), 500)
    }
}
