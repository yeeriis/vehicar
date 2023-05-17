import { Component, OnInit } from '@angular/core';
import { CarsService } from '../cars-cards/cars-cards.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cars-cards',
  templateUrl: './cars-cards.component.html',
  styleUrls: ['./cars-cards.component.css']
})
export class CarsCardsComponent implements OnInit {
  cars: any;

  constructor(private carsService: CarsService, private router: Router) { }

  ngOnInit() {
    this.getCars();
  }

  getCars() {
    this.carsService.getCars().subscribe(
      data => {
        this.cars = data;
      },
      error => {
        console.log(error);
      }
    );
  }

  
}
