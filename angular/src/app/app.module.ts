import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LoginComponent } from './login/login.component';
import { AdminComponent } from './admin/admin.component';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { FooterComponent } from './footer/footer.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CarsCardsComponent } from './cars-cards/cars-cards.component';
import { CarDetailComponent } from './car-detail/car-detail.component';
import { UserRegisterComponent } from './user-register/user-register.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { MainCarrouselComponent } from './main-carrousel/main-carrousel.component';
import { HomeComponent } from './home/home.component';
import { CarLeasingComponent } from './car-leasing/car-leasing.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    AdminComponent,
    AdminLoginComponent,
    FooterComponent,
    NavbarComponent,
    CarsCardsComponent,
    CarDetailComponent,
    UserRegisterComponent,
    UserProfileComponent,
    MainCarrouselComponent,
    HomeComponent,
    CarLeasingComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
