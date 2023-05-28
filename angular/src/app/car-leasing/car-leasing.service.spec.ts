import { TestBed } from '@angular/core/testing';

import { CarLeasingService } from './car-leasing.service';

describe('CarLeasingService', () => {
  let service: CarLeasingService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CarLeasingService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
