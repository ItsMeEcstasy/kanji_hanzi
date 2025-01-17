img = imread('images_go_here');
img = img(:,:,1);

out = double(img);
sz = size(out);
for ii=1:sz(1)
   for jj=1:sz(2)
      old = out(ii,jj);
      %new = 255*(old >= 128); % Original Floyd-Steinberg
      new = 255*(old >= 128+(rand-0.5)*100); % Simple improvement
      out(ii,jj) = new;
      err = new-old;
         if jj<sz(2)
            % right
            out(ii  ,jj+1) = out(ii  ,jj+1)-err*(7/16);
         end
      if ii<sz(1)
         if jj<sz(2)
            % right-down
            out(ii+1,jj+1) = out(ii+1,jj+1)-err*(1/16);
         end
            % down
            out(ii+1,jj  ) = out(ii+1,jj  )-err*(5/16);
         if jj>1
            % left-down
            out(ii+1,jj-1) = out(ii+1,jj-1)-err*(3/16);
         end
      end
   end
end

imshow(out)
