import { Component, Input, OnChanges, ViewChild, Output, EventEmitter } from '@angular/core';
import {NgbModal, NgbActiveModal} from '@ng-bootstrap/ng-bootstrap';
import { faTimes } from '@fortawesome/free-solid-svg-icons';

@Component({
    selector: 'app-tags-modal',
    templateUrl: './tags-modal.component.html',
    styleUrls: ['./tags-modal.component.scss']
})
export default class TagsModalComponent {
    faTimes = faTimes;
    @ViewChild('content') content: any;

    constructor(
        private modalService: NgbModal
    ) {}

    @Input() opened = false;
    @Input() tags: any[] = [];
    @Output() closed = new EventEmitter<any>();

    selectedTags = [];
    modal;

    ngOnChanges(){
        if (this.opened){
            this.open();
        }
    }

    selectTag = (tag) => {
        if (this.selectedTags.indexOf(tag) < 0){
            this.selectedTags.push(tag);
        }
    }

    removeSelectTag = (tag) => {
        if (this.selectedTags.indexOf(tag) > -1){
            this.selectedTags = this.selectedTags.filter(item => (item !== tag) );
        }
    }

    sure = () => {
        this.modal.dismiss(this.selectedTags);
    }

    open(): void {
        this.modal = this.modalService.open(this.content, {size: 'lg'});
        this.modal.closed.subscribe(value => {
            console.log(value);
        });

        this.modal.dismissed.subscribe(value => {
            this.closed.emit(value);
        });
    }

}
