import { Component } from "@angular/core";
import { NgbActiveModal, NgbModal } from "@ng-bootstrap/ng-bootstrap";
import { AuthService } from "app/api/auth.service";

@Component({
    // tslint:disable-next-line: component-selector
    selector: "ngbd-modal-confirm",
    templateUrl: "./login.modal.html"
})
export class LoginModalComponent {
    public email;
    public password;
    public auth;
    public message = "";

    constructor(public modal: NgbActiveModal, auth: AuthService) {
        this.auth = auth;
    }
    login() {
        this.auth
            .login({ email: this.email, password: this.password })
            .subscribe(
                resp => {},
                err => {
                    if (err.error.errors) {
                        this.message = err.error.message;
                    }
                }
            );
    }
}
