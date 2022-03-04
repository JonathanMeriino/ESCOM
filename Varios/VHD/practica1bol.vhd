library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;
entity boleta is port(
	clk: in std_logic;                 
	d: out std_logic_vector(3 downto 0);
	aux: out std_logic_vector (3 downto 0));
				
end boleta;
architecture no_boleta of boleta is

 begin
	process (clk) begin
		if (clk'event and clk='1')then
			aux <= aux+1;
			if (aux="1001") then
				aux<="0000";
			 end if;
		end if;
	end process;
	process (aux) begin
	case aux is
	
	when "0000"=> d: = "0010"; --2
			
	when "0001"=> d: = "0000"; --0
			
	when "0010"=> d: = "0100"; --4
			
	when "0011"=> d: = "0011";--3
			
	when "0100"=> d: = "0001";--1
			
	when "0101"=> d: = "0101";--5
			
	when "0110"=> d: = "0111"; --7
			
	when "0111"=> d: = "1001"; --9
			
	when "1000"=> d: = "0110"; --6
			
	when "1001"=> d: = "0011"; --3
			
	when others=> d: = "1111"; 
			
	end case;
	end process;
end no_boleta;