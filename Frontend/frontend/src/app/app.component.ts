import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  testUser = {
    username: "admin",
    status: "online",
    contacts: ["friend"],
    past_chats: ["chat 1","chat 2","chat 3"]
  }
}
