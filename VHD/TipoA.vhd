-- TipoA
library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;

entity hola is port(
	
	sal: in std_logic_vector (3 downto 0);
	letra: out std_logic_vector(6 downto 0));
end hola;

architecture holas of hola is
 begin

	proces: process (sal) begin
	case sal is
	when "0111" => letra <= "0110111";--H
	when "1011" => letra <= "1111110";--O
	when "1101" => letra <= "0001110";--L
	when "1110" => letra <= "1110111";--A
	when others=>  letra <= "1111111";
	
	end case;
	
	end process proces;
end holas;