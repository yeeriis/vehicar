import { TestBed } from '@angular/core/testing';

import { CarsCardsService } from './cars-cards.service';

describe('CarsCardsService', () => {
  let service: CarsCardsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CarsCardsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
