function [fitresult, gof] = plot2(n, t_w)
%CREATEFIT(N,T_W)
%  Create a fit.
%
%  Data for 'untitled fit 1' fit:
%      X Input : n
%      Y Output: t_w
%  Output:
%      fitresult : a fit object representing the fit.
%      gof : structure with goodness-of fit info.
%
%  另请参阅 FIT, CFIT, SFIT.

%  由 MATLAB 于 18-Nov-2020 21:49:55 自动生成


%% Fit: 'untitled fit 1'.
[xData, yData] = prepareCurveData( n, t_w );

% Set up fittype and options.
ft = fittype( 'power2' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display = 'Off';
opts.StartPoint = [0.190436719337763 0.662986379671419 8.2442756658209];

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );

% Plot fit with data.
figure( 'Name', 'untitled fit 1' );
plot( fitresult, xData, yData );
% Label axes
xlabel('the number of vertices')
ylabel('t')
% xlabel( 'n', 'Interpreter', 'none' );
% ylabel( 't_w', 'Interpreter', 'none' );
grid on


