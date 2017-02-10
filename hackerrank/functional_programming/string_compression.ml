open Core.Std;;

let char_stream_of_channel channel = 
  Stream.from
    ( fun _ -> try Some (input_char channel) with End_of_file -> None);;

let compress stream =
  let rec aux 

let () =
  let stream = char_stream_of_channel stdin in
