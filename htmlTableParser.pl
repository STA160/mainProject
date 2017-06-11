#!/usr/bin/perl

#~ use strict;
use warnings; 

##You will need to download the two bottom packages from CPAN
use HTML::TableExtract;
use Text::Table;

##
#
#
#
##

my $doc = 'cleanedTableData.html';

my $headers =  [ 'State Name', 'Approve', 'Disapprove', 'Senator', 'Party' ];
 
my $table_extract = HTML::TableExtract->new(headers => $headers);
my $table_output = Text::Table->new(@$headers);
 
$table_extract->parse_file($doc);
my ($table) = $table_extract->tables;

print @$headers[0] . ',' . @$headers[1] . ',' . @$headers[2] . ',' . @$headers[3] . ',' . @$headers[4] . ',' .  "Name";
print "\n";

my @nuSenatorName; #this adds a new name to upper case so we can better grep the name in R



#~ 
#~ my $tempString; 
for my $row ($table->rows) {
    #~ clean_up_spaces($row); # not shown for brevity
    #~ $tempString = @$row[3]; 
    
	@nuSenatorName = split(' ', @$row[3]); #this is the split name right here
	#translate to something else
	
	#strip the percents of the value strings, and just leave the numbers 
	 

	@$row[1] =~ s/%//g; #turn % into blank
	@$row[2] =~ s/%//g; #turn % into blank
	
    print @$row[0] . ',' . @$row[1] . ',' . @$row[2] . ',' . @$row[3] . ',' . @$row[4] . ',' . uc ($nuSenatorName[1]); #this shouuld work 
    #~ print $tempString .  "\n";
    print "\n";
    #~ $table_output->load($row);
}
 
