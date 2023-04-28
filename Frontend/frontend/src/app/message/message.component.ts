import { Component, Input } from '@angular/core';
import { Message } from '../chat.service';

@Component({
  selector: 'app-message',
  template: `
    <body *ngIf="message">
      <h3>{{ message.username }}</h3>
      <div *ngIf="isString()">
        <h5>{{ decodeString() }}</h5>
      </div>
      <div *ngIf="!isString()">
        <h5> Non string messages not implemented yet! </h5>
      </div>
      <p class="date">{{ message.date }}</p>
    </body>
    <body *ngIf="!message">
      <p class="loading">!!! LOADING !!!</p>
    </body>
  `,
  styles: [
    'body { background-color: #ff9800; border-radius: 50px; border: thin, black; margin: 5px; padding: 0px 40px}',
    'h3 { color: white; text-shadow: 2px 2px black; text-decoration: underline }',
    'h5 { color: white; text-shadow: 1px 1px black; }',
    '.date { color: black; text-shadow: 1px 1px white; }'
  ]
})
export class MessageComponent {
    @Input() message: Message;
    constructor() { }

    isString(): boolean {
      return this.message.type == "str";
    }

    decodeString(): string {
      return this.message.message.toString();
    }
}
