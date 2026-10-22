
/*
Original: Check_all_servers.go + Config_details.go
These were WLST snippets calling connect() and ls()
Clean Go version that lists servers via REST API - safe to publish

Attach this file to show Go knowledge (Nice to have for Askable)
*/
package main

import "fmt"

type ServerRuntime struct {
    Name  string
    State string
    Health string
}

func GetServerRuntimes() []ServerRuntime {
    // Mock - replace with real REST call to /management/weblogic/latest/serverRuntimes
    return []ServerRuntime{
        {Name: "AdminServer", State: "RUNNING", Health: "HEALTH_OK"},
        {Name: "soa_server1", State: "RUNNING", Health: "HEALTH_OK"},
        {Name: "osb_server1", State: "RUNNING", Health: "HEALTH_WARN"},
    }
}

func main() {
    for _, s := range GetServerRuntimes() {
        fmt.Printf("%s %s\n", s.Name, s.State)
    }
}
