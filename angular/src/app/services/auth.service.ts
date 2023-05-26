import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  isAuthenticated(): boolean {
    return localStorage.getItem('token') !== null; // Verifica si el token está presente en el almacenamiento local
  }

  getToken(): string {
    return localStorage.getItem('token'); // Obtiene el token del almacenamiento local
  }
}
