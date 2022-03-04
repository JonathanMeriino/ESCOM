library ieee;
use ieee.std_logic_1164.all;

entity mario_en is
	Port (
			clk: in std_logic;
			sen: inout bit;  -- señal
			enable: in bit;   -- enable
			mario_adv:inout bit;	--avanzar
			Vec_mario:inout bit_vector(0 to 7); -- muestra la salida
			sal_boton:inout bit;
			suelo:inout bit_vector(0 to 7)
			);

end mario_en;

architecture mario_arq of  mario_en is

 -- vector mario
signal en_mario : bit:='1';   -- mueve el circuito, meten datos de manera seriada, recorrer datos
signal fn_mario : bit:='0';

signal mariojump: bit_vector(0 to 7 );
signal knoptsal: bit:='0'; -- detecta que esta en el aire



	begin

	process(enable, clk,sen,en_mario,fn_mario,vec_mario) -- reset señal sensitiva
		begin
		if rising_edge(clk) then
				if(enable='1') then
						vec_mario <= "00000000";
						suelo<="11111111";
						
				else
				suelo<="11011011";

			if (mario_adv ='1') then
			--mueve vector mario
				vec_mario(0) <= (sen and en_mario) or (fn_mario and vec_mario(1));

	        for i in 1 to 6 loop

				vec_mario(i) <= (vec_mario(i-1) and en_mario) or (fn_mario and vec_mario(i+1));

	        end loop;
	        		vec_mario(7) <= (vec_mario(6) and en_mario) or (fn_mario and sen);
			--termina vector mario
			else
			    vec_mario <= vec_mario; -- guardar el dato sin perderlo
		 	end if ;
		end if;


		-- salto vertical
		if (Sal_boton='1'and mario_adv='0') then
			knoptsal<='1';
			mariojump <= vec_mario;
			vec_mario<= "00000000";
		-- salto diagonal	
		elsif (Sal_boton='1'and mario_adv='1') then
			knoptsal<='1';
			mariojump (0) <= (sen and en_mario) or (fn_mario and vec_mario(1));

		for i in 1 to 6 loop

			mariojump(i) <= (vec_mario(i-1) and en_mario) or (fn_mario and vec_mario(i+1));

		end loop;
		mariojump (7) <= (vec_mario(6) and en_mario) or (fn_mario and sen);
		vec_mario <= "00000000";

		end if ;
		-- baja de forma vertical
		if (knoptsal = '1'and mario_adv='0') then
			vec_mario<= mariojump;
			mariojump <= "00000000";
			knoptsal <= '0';
			sal_boton <= '0';
		-- baja en diagonal
		elsif(knoptsal = '1' and mario_adv='1')then
			vec_mario(0) <= (sen and en_mario) or (fn_mario and mariojump(1));

				for i in 1 to 6 loop

					vec_mario(i) <= (mariojump(i-1) and en_mario) or (fn_mario and mariojump(i+1));

				end loop;
				vec_mario(7) <= (mariojump(6) and en_mario) or (fn_mario and sen);
				mariojump <= "00000000";
				knoptsal <= '0';
				sal_boton <= '0';

		end if;

						for i in 0 to 6 loop
							-- cuando cumple la funcion caninoca mario muere
								if ((Vec_mario(i) and not  suelo(i))='1') then
									-- reinicia sin mario
									Vec_mario <="00000000";
									mariojump<="00000000";
									
									suelo<="11011011";
								end if ;
						end loop;


	    	end if;
	     -- vector que suma

	end process;

	process (vec_mario,sal_boton) -- si no existe un mario, lo agrega

		begin
			if ((vec_mario(0)or vec_mario(1)or vec_mario(2)or vec_mario(3)or vec_mario(4)or vec_mario(5)or vec_mario(6)or vec_mario(7)or Sal_boton )='0') then -- suma las señales de los vectores
				sen<='1';

			else

    			sen<='0';

			end if;

	end process;



end architecture;