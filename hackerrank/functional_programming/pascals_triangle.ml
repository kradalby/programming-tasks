let factorial number =
  let rec aux acc = function
    | 0 -> acc
    | n -> aux (acc*n) (n-1)
  in
  aux 1 number;;

let pascals_triangle_formula row column =
  (factorial row / ((factorial column) * (factorial (row - column))));;


let pascals_triangle_row row column =
  let rec aux acc r c = 
    match c with 
    | 0 -> acc
    | _ -> aux (acc@[(pascals_triangle_formula row (c-1))]) row (c-1) 
  in
  aux [] row column;;


let pascals_triangle number =
  let rec aux acc = function 
    | 0 -> ((pascals_triangle_row 0 1)::acc)
    | n -> aux ((pascals_triangle_row n (n+1))::acc) (n-1)
  in
  aux [] (number-1);;


let () =
  let number = read_int() in
  let pyr = pascals_triangle number in
  List.iter (fun row -> (print_endline (String.concat " " (List.map (fun element -> string_of_int element ) row)))) pyr