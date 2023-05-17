import { Injectable, ErrorHandler } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { Coche } from '../car-detail/car.model';
import { tap, catchError } from 'rxjs/operators';




@Injectable({
  providedIn: 'root'
})
export class CarsService {
  apiUrl = 'http://localhost:8000/api/coches';

  baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) { }

  getCars() {
    return this.http.get(this.apiUrl)
      .pipe(
        map((response: any) => {
          return response.coches;
        })
      );
  }

  getCochesById(id: number): Observable<Coche>{
    const url = `${this.apiUrl}/${id}`;
    console.log(url);
    return this.http.get(url)
    .pipe(
      map((response: any) => {
        return response.coches;})
    );
  }
}
