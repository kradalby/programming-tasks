open Core.Std;;

let rec read_lines () =
  try let line = read_line () in
    line :: read_lines()
  with
    End_of_file -> []

let permute str = 
  let stream = Stream.of_string str in
  Stream.from (fun _ -> 
      try 
        let x = Stream.next stream in
        let y = Stream.next stream in
        Some ((Char.to_string y) ^ (Char.to_string x)) 
      with 
        End_of_file -> None);;

let us_do_this_shit word = 
  try
    Stream.iter (fun c -> print_string c) (permute word)
  with Stream.Failure ->
    print_endline "";;

let () = 
  let _ = read_int() in
  let arr = read_lines() in
  List.iter arr (fun word -> us_do_this_shit word);;