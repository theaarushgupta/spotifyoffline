<p align = "center">
    <a href = "https://opensource.org/licenses/MIT">
        <img alt = "License" src = "https://img.shields.io/badge/License-AGPLv3-green.svg">
    </a>
</p>

<h1 align = "center">Spotify Offline <code>v0.0.1</code></h1>
<h3 align = "center">listen to your favorite spotify songs, offline</h3>

# Overview

Spotify Offline (`spotifyoffline`) is a command line tool that allows one to download Spotify playlists in MP3 format. It is built to serve as a free and open-sourced substitute to Spotify's priced offline streaming.

# Examples

## Basic Usage

Before downloading music from a Spotify playlist, credentials and the playlist ID must be defined in a YAML configuration/credentials file. An example of this can be found in `credentials.sample.yml`.

Resources for finding the playlist ID can be found [here](https://clients.caster.fm/knowledgebase/110/How-to-find-Spotify-playlist-ID.html) and those for getting the credentials for the Spotify API can be found [here](https://developer.spotify.com/documentation/general/guides/app-settings/).

One can begin the download process by running `spotifyoffline <credentials>`, replacing `credentials` with the path to the YAML file.

# Copyright &copy; 2021 Aarush Gupta
This code is copyrighted but licensed to the public under the GNU AGPLv3 license and any later versions.
