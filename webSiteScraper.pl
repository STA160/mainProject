#!/usr/bin/perl

use strict; 
use warnings; 
#~ use JSON; 
#~ use WWW::Mechanize;
#~ my $mech = WWW::Mechanize->new();

my @siteArray; 
#~ my $url = "https://www.supremecourt.gov/oral_arguments/argument_transcript.aspx";
#~ my $baseUrl = "https://www.supremecourt.gov/oral_arguments/";
my $file = $ARGV[0] or die "file input not selected!\n";

open('FILE',"< $file") or die "error openning file" ; #open the fd or die

while(<FILE>)
{
	
	chomp($_); #chomp data
	#~ push(@siteArray,$_ ); #push the data on the stack
	#~ print $baseUrl . $_ . "\n"; 
	
	`wget $_`; #this is getting everything right here
	sleep(int(rand(18))); #for sleeping before fetching more data

}


close(FILE);

exit 0; 

#~ my $i = 0; 

#~ for ($i = 0; $i < @siteArray; $i++)
#~ {
	#~ $mech->get($siteArray[$i]);
	 
	#~ $mech->links();
	#~ $mech->dump_links();

	 
	 
	 #~ sleep(int(rand(18))); #for sleeping before fetching more data
	
#~ #	#~ rand(1); #just putting this here temporary 
#~ }


#~ print $links; 	
#~ my $curlVar = `curl http://www.google.com`; 
#~ $mech->
#~ print $curlVar; 
#~ my $urlString;  #main url string

#~ my $temporaryBuffer = ""; #this is a buffer


#~ my $i = 0;

#~ for ($i = 0; $i < 100; $i++)
#~ { 

	#~ $temporaryBuffer = `curl $urlString > /dev/shm/temp.html`


#~ }


 
