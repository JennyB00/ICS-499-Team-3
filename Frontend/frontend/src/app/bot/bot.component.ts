import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpParams } from '@angular/common/http';
import { UserService } from '../user.service';

@Component({
  selector: 'app-bot',
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css']
})

export class BotComponent implements OnInit{
  messages: listItem[] = [];
  prompt: string = '';
  generateImg: boolean = false;
  imgURL: string;
  imgPreview: boolean = true;
  isLoading: boolean = true;

  constructor(private router: Router, private http: HttpClient, private userService: UserService) {}

  ngOnInit(): void {
    if (!this.userService.isLoggedIn()) {
      this.router.navigate(["/"]);
    }
  }

  submit() {
    this.isLoading = true;
    if (this.prompt.trim() !== '') {
      // send the message to the server using POST request
      this.messages.push({type: "prompt",message: this.prompt});
      this.http.post<string>('/bot/process','', { params: new HttpParams().set('prompt',this.prompt).set('username',this.userService.getCurrentUser())})
        .subscribe({
          next: (response) => {
            console.log('Message sent successfully');
            console.log('Response:', response);
            this.messages.push({type: "response",message: response.toString()});
            this.isLoading = false;
            this.prompt = '';
          },
          error: (error) => {
            console.error('Error sending message: ', error);
            console.log('Error response body: ', error.error);
            this.isLoading = false;
          }
        });
    }
  }

  onKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter' && this.prompt.trim() !== '') {
      this.submit();
    }
  }

  generate() {
    if (this.prompt.trim() !== '') {
      this.imgURL = '';
      this.http.post<string>('/bot/generate_image','', {params: new HttpParams().set('prompt',this.prompt)}).subscribe(
        (url) => {
          this.imgURL = url;
        });
        this.prompt = '';
      }
  }

  onGenerate() {
    this.generateImg = true;
  }

  onChat() {
    this.generateImg = false;
  }

  onImgClick() {
    const flip = !this.imgPreview;
    this.imgPreview = flip;
  }
}

interface listItem {
  type: string;
  message: string;
}
