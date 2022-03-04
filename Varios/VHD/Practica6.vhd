library IEEE;
use IEEE.std_logic_1164.all;

entity practica6 is
    port (
        sen0, sen1, opc0, opc1, opc2, opc3 : in std_logic );
	salida : out std_logic;	
		
end practica6;

architecture Behavioral of practica6 is

signal sel: std_logic_vector (1 downto 0);

begin

    sel(1) <= sen1;
    sel(0) <= sen0;

    salida <= opc0 when sel = "00" else
        opc1 when sel = "01" else
        opc2 when sel = "10" else
        opc3 when sel = "11" else
        'U';

end Behavioral;