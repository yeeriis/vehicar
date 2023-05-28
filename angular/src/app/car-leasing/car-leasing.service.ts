import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CarLeasingService {
  private url = 'http://localhost:8000/api/register-leasing/';

  constructor(private http: HttpClient) { }

  registrarAlquiler(email_usuario: any) {
    return this.http.get(this.url, email_usuario);
  }
}
