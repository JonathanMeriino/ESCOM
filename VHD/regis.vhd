library ieee;
use ieee.std_logic_1164.all;

entity pines is 
port(P: in std_logic_vector(3 downto 0);
	CLK,LOAD: in std_logic;
	Q : out  std_logic_vector(3 downto 0));
end pines;

architecture Behavioral of pines is 

begin 

process(CLK,P,LOAD)

begin
	if (CLK'event and CLK ='1') then 
		if LOAD='1' then
		Q <= P;
		end if;
		end if;
end process;


end Behavioral;