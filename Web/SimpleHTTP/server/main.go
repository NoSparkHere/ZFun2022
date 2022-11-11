package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		io.WriteString(w, "The first challenge is at /flag1. GET it first!")
	})

	http.HandleFunc("/flag1", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "GET" {
			io.WriteString(w, "\"We usually GET things from servers...\"\nVisit /f1ag2 for next challenge. Not the letter 'l'!")
		} else {
			io.WriteString(w, "You used a wrong method! You need to GET the flag.")
		}
	})

	http.HandleFunc("/f1ag2", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "POST" {
			io.WriteString(w, "\"...and POST our forms to them.\"\nVisit /flag333 for next challenge.")
		} else {
			io.WriteString(w, "The flag hides deep! You need to POST for it.")
		}
	})

	http.HandleFunc("/flag333", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Add("Set-Cookie", "Quote=Sometimes we eat Cookies...")
		w.Header().Add("Set-Cookie", "NextChallenge=/f_l_a_g_4")
		io.WriteString(w, "Cookies are delicious!")
	})

	http.HandleFunc("/f_l_a_g_4", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Add("Quote", "...through_the_magic_of_Headers")
		w.Header().Add("Flag", "ZFun{You_learnt_s1mple_HTTP!}")
		io.WriteString(w, "But how does the server send cookies to us?")
	})

	log.Fatal(http.ListenAndServe("0.0.0.0:10003", nil))
}
