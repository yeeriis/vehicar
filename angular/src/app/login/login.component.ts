import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  email: string;
  password: string;

  constructor(private http: HttpClient, private router:Router) {}

  login() {
    
    const data = { email: this.email, password: this.password };
    this.http.post('http://localhost:8000/api/login/', data).subscribe(
      (response) => {
        console.log(response);
        this.router.navigate(['']);
      },
      (error) => {
        console.error(error);
        alert("Error!")
      }
    );
  }
}
