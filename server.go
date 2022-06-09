package main

import (
	"fmt"
	"net/http"
	"os"

	cowsay "github.com/Code-Hex/Neo-cowsay/v2"
	"github.com/labstack/echo/v4"
)

func main() {
	hostname, err := os.Hostname()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	version := os.Getenv("VERSION")
	if version == "" {
		version = "N/A"
	}
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		msg := c.QueryParam("message")
		if msg == "" {
			msg = "Nothing to say?"
		}
		say, err := cowsay.Say(
			msg,
			cowsay.Type("default"),
			cowsay.BallonWidth(40),
		)
		say = say + fmt.Sprintf("\n\nfrom: %v\nversion: %v", hostname, version)
		if err != nil {
			return c.String(http.StatusInternalServerError, "No cows around!")
		}
		return c.String(http.StatusOK, say)
	})
	e.Logger.Fatal(e.Start(":8080"))
}
