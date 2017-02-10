open Core.Std;;

type grid = char list list

let tup = fun a b -> (a, b)

let print_grid grid =
  List.iter grid 
    (fun r -> print_endline 
        (String.concat 
           (List.map r
              (fun c -> String.of_char c))))

let read_grid rows = 
  let rec aux acc = function
    | 0 -> acc
    | n -> aux (acc@[(String.to_list (read_line()))]) (n-1)
  in
  aux [] rows ;;


(* 'o' expresses out of bounds, probably not optimal *)
let get_cell (grid : grid) (row, col) = 
  match (List.nth grid row) with
  | None -> 'o'
  | Some lst ->
    match (List.nth (lst) col) with
    | None -> 'o'
    | Some c -> c

let get_edges (grid : grid) (row, col) =
  List.filter_map 
    (* Top, left, right, bottom*)
    [(-1, 0); (0, -1); (0, 1); (1,0)] 
    (fun (r, c) ->
       match (get_cell grid ((row-r), (col-c))) with
       | '-' -> Some ((row-r), (col-c))
       | '.' -> Some ((row-r), (col-c))
       | _ -> None)


let dfs (grid : grid) start goal =
  let rec aux visited = function


    let () =
      let pacman = (Scanf.sscanf (read_line()) "%d %d" tup) in
      let food = (Scanf.sscanf (read_line()) "%d %d" tup) in
      let (size_r, size_c) = (Scanf.sscanf (read_line()) "%d %d" tup) in
      let grid = read_grid size_r in
      print_grid grid;
      print_endline (String.of_char ( get_cell grid (0, 0)));
      List.iter (get_edges grid pacman) 
        (fun (r,c) -> print_endline ((string_of_int r) ^ " " ^ (string_of_int c)));;