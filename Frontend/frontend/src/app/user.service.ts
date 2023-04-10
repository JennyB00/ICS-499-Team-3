import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  users = [
    {
      username: "admin",
      status: "online",
      contacts: ["friend"],
      past_chats: ["123","456","789"]
    },
    {
      username: "friend",
      status: "offline",
      contacts: [],
      past_chats: ["456"]
    }
  ];
  currentUser: string = '';
  constructor() { }

  getAll() {
    return this.users;
  }

  get(username: string) {
    for (var user of this.users) {
      if (user.username == username) {
        return user
      }
    }
    return
  }
  
  add(user: any) {
    this.users.push(user);
  }

  addContact(username: string, contact: string) {
    for (var user of this.users) {
      if (user.username == username) {
        user.contacts.push(contact)
      }
    }
  }

  delete(user: any) {
    const index = this.users.indexOf(user)
    if (index >= 0) {
      this.users.splice(index, 1)
    }
  }

  getUsernames() {
    return ['admin','friend']
  }

  verifyPassword(username: string, password: string) {
    return true;
  }

  setCurrentUser(username: string) {
    this.currentUser = username;
  }

  getCurrentUser() {
    return this.currentUser;
  }

  isLoggedIn() {
    return this.currentUser == '' ? false : true;
  }
}
