-- Tipo Z
library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;
entity hola is port( 
	sal: in std_logic_vector (3 downto 0);
	letra: out std_logic_vector(6 downto 0)); 
end hola;
architecture holas of hola is
 begin

	process (sal) begin
	
	case sal is
	when "1000" => 	letra <= "0110111";
	when "0100" => 	letra <= "1111110";
	when "0010" => 	letra <= "0001110";
	when "0001" => 	letra <= "1110111";
	when others=>  	letra <= "1111111";
	end case;

	end process;
end holas;