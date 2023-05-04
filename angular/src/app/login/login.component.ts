import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  email: string;
  password: string;

  constructor(private http: HttpClient) {}

  login() {
    const data = { email: this.email, password: this.password };
    this.http.post('http://localhost:8000/api/auth/login/', data).subscribe(
      response => {
        console.log(response);
        alert("Acierto!")
      },
      error => {
        console.error(error);
        alert("Error!")
      }
    );
  }
}
