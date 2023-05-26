import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';
import { LoginService } from './login.service';




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  email: string;
  password: string;

  constructor(private http: HttpClient, private router:Router, private loginService: LoginService) {}

  login() {
    
    const data = { email: this.email, password: this.password };
    this.http.post('http://localhost:8000/api/login/', data).subscribe(
      (response: any) => {
        console.log(response);

        localStorage.setItem('token', response.token);
        // localStorage.setItem('access_token', response.access);
        // localStorage.setItem('refresh_token', response.refresh);

        this.router.navigate(['']);
      },
      (error) => {
        console.error(error);
        alert("Error!")
      }
    );
  }

  // logueo() {
  //   this.loginService.logueo(this.email, this.password).subscribe(
  //     (response) => {
  //       // Manejar el éxito de inicio de sesión
  //       console.log('Inicio de sesión exitoso', response);
  //     },
  //     (error) => {
  //       // Manejar el error de inicio de sesión
  //       console.log('Error de inicio de sesión', error);
  //     }
  //   );
  // }
}
