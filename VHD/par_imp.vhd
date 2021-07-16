library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity par is 
port(
	A,B,C:in std_logic;
	PAR,IMPAR : out std_logic);
end PAR;

architecture funcionamiento of par is
	
	begin

		PAR <= (B and not C) or (A and not C);
		IMPAR <= C;

end funcionamiento;
