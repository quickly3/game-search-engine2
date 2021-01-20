import { Component, ViewEncapsulation } from "@angular/core";

import { Observable, of } from "rxjs";
import { debounceTime, map, switchMap, tap, catchError } from "rxjs/operators";
import { GameService } from "../api/game.service";

@Component({
    // tslint:disable-next-line: component-selector
    selector: "games",
    templateUrl: "./games.component.html",
    styleUrls: ["./games.component.scss"]
})
export class GamesComponent {
    game_list = [];
    total_number = 0;
    current_page = 1;
    row = 10;
    game_keywords = "";
    gameService;

    constructor(gameService: GameService) {
        this.gameService = gameService;
    }

    // tslint:disable-next-line: use-life-cycle-interface
    ngOnInit(): void {
        this.getGameDatas();
    }

    searchKeyDown = (event: any) => {
        if (event.key === "Enter") {
            this.getGameDatas();
        }
    };

    getGameDatas = () => {
        let params = {
            page: "" + this.current_page,
            keywords: this.game_keywords
        };

        this.gameService.getGamesApi(params).subscribe(data => {
            this.game_list = data["data"];
            this.game_list.map(item => {
                item.unfold = false;
            });
            this.total_number = data["total"];
        });
    };

    getGameDatasSimple = (term: any) => {
        let params = {
            page: "1",
            keywords: term,
            search_type: "simple"
        };
        return this.gameService.getGameDatasSimpleApi(params).pipe(
            map(response => {
                let names = response["data"].map(item => item.name);
                return names;
            })
        );
    };

    pageChange = () => {
        this.getGameDatas();
    };
    search = () => {
        this.getGameDatas();
    };
    // search_by_keywords = ()=>{}
    search_by_keywords = (text$: Observable<string>) =>
        text$.pipe(
            debounceTime(300),
            tap(),
            switchMap(term =>
                this.getGameDatasSimple(term).pipe(
                    tap(),
                    catchError(() => {
                        return of([]);
                    })
                )
            )
        );

    searchMore = $event => {
        this.game_keywords = $event.item;
        this.search();
    };

    toggleUnfold = game => {
        game.unfold = !game.unfold;
    };
}
