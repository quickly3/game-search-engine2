import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { LoginModalComponent } from "./login/login.modal";
import { FormsModule } from "@angular/forms";

@NgModule({
    imports: [CommonModule, FormsModule],
    declarations: [LoginModalComponent],
    exports: [CommonModule, LoginModalComponent],
    entryComponents: [LoginModalComponent]
})
export class ModalsModule {}
